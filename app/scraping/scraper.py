import pprint
import random
from datetime import datetime, timedelta
import asyncio
import logging
from playwright.async_api import async_playwright, TimeoutError
from tzlocal import get_localzone


local_tz = get_localzone()

logger = logging.getLogger('scraper')
logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)s %(message)s %(asctime)s')


class ArticleParser:

    article_date_classes = ['o-teaser__timestamp', 'stream-card__date']
    article_header_class = 'o-teaser__heading'
    article_subtitle_class = 'o-teaser__standfirst'

    async def parse_article(self, article, details=False) -> dict:
        data = {}
        # if article.find('div', class_='o-ads') or article.find('div', class_='o-teaser--native-ad'):
        #     return data

        # for date_class in self.article_date_classes:
        #     time_div = article.find('div', class_=date_class)
        #     if time_div:
        #         break
        # raw_date = time_div.find('time').get('datetime')
        # if raw_date.endswith('Z'):
        #     raw_date = raw_date.replace('Z', '+00:00')
        # elif raw_date.endswith('+0000'):
        #     raw_date = raw_date[:-5] + '+00:00'
        # pub_date = datetime.fromisoformat(raw_date).astimezone(local_tz)
        # data.update({'published_at': pub_date,
        #              'scraped_at': datetime.now()})
        # header = article.find('div', class_=self.article_header_class)
        # link = header.find('a')
        # data.update({'url': f"{self.site_base_url + link.get('href')}", 'title': link.text})
        # image = article.find('img')
        # data.update({'image_url': image.get('data-src')})
        # subtitle_p = article.find('p', class_='o-teaser__standfirst')
        # data.update({'subtitle': subtitle_p.text})

        return data

    async def collect_publication_date(self, article):
        for date_class in self.article_date_classes:
            time_div = await article.query_selector(f'div.{date_class}')
            if time_div:
                div_class = await time_div.get_attribute('class')
                if 'live' not in div_class:
                    break
        time_element = await time_div.query_selector('time')
        raw_date = await time_element.get_attribute('datetime')
        if raw_date.endswith('Z'):
            raw_date = raw_date.replace('Z', '+00:00')
        elif raw_date.endswith('+0000'):
            raw_date = raw_date[:-5] + '+00:00'
        pub_date = datetime.fromisoformat(raw_date).astimezone(local_tz)
        return pub_date

    async def collect_link_and_title(self, article):
        header = await article.query_selector(f'div.{self.article_header_class}')
        link_element = await header.query_selector('a')
        link = await link_element.get_attribute('href')
        title = await link_element.text_content()
        return link, title

    async def collect_image(self, article):
        image = await article.query_selector('img')
        image_url = await image.get_attribute('data-src')
        return image_url

    async def collect_subtitle(self, article):
        subtitle_p = await article.query_selector(f'p.{self.article_subtitle_class}')
        if subtitle_p:
            text = await subtitle_p.text_content()
            return text

    async def parse_preliminary_information(self, article):
        if await article.query_selector(f'div.o-ads') or await article.query_selector('div.o-teaser--native-ad'):
            return None

        data = {'scraped_at': datetime.now()}
        pub_date = await self.collect_publication_date(article)
        data.update({'published_at': pub_date})
        link, title = await self.collect_link_and_title(article)
        data.update({'url': link, 'title': title})
        image_url = await self.collect_image(article)
        data.update({'image_url': image_url})
        subtitle = await self.collect_subtitle(article)
        data.update({'subtitle': subtitle})
        return data

    async def parse_page(self, page, border_date):
        parsed_articles, continue_scraping = [], True
        articles_list = await page.query_selector('ul.o-teaser-collection__list')
        articles = await articles_list.query_selector_all('li')
        for article in articles:
            parsed_article = await self.parse_preliminary_information(article)
            if parsed_article:
                if parsed_article.get('published_at') < border_date:
                    continue_scraping = False
                    break
                parsed_articles.append(parsed_article)
        return parsed_articles, continue_scraping

class Scraper:

    # ~65 pages to get all articles for month
    # ~ 25 articles per page
    # ~ 1600 articles

    article_class = 'o-teaser'
    site_base_url = 'https://www.ft.com'

    def __init__(self, starting_path: str, first_try=False):
        self.url = f'{self.site_base_url}{starting_path}'
        self.current_page = 1

        current_date = datetime.now().astimezone(local_tz)
        date_timeout = timedelta(days=30) if first_try else timedelta(hours=1)
        self.border_date = current_date - date_timeout
        self.parser = ArticleParser()
        self.first_try = first_try

    async def collect_articles_preliminary_information(self, page):
        """
        Collects articles information that can be accessed from articles list. Such as article url, title, subtitle,
        publication date
        :return:
        """
        articles = []
        continue_scraping = True
        logger.info('Collecting preliminary articles information')

        while continue_scraping:
            logger.info(f'Scraping page {self.current_page}')
            await page.goto(f'{self.url}?page={self.current_page}')
            await page.wait_for_timeout(1000)
            parsed_articles, continue_scraping = await self.parser.parse_page(page, self.border_date)
            articles.extend(parsed_articles)

            waiting_time = random.uniform(5, 10)
            logger.info(f'waiting {waiting_time} seconds before continue')
            await asyncio.sleep(waiting_time)

            self.current_page += 1

        logger.info('Preliminary information collected')
        return articles

    async def check_session(self, page):
        try:
            await page.goto(self.url)
            await page.wait_for_timeout(3000)
            await page.wait_for_selector("#o-header-top-link-myaccount", timeout=5000)
            return True
        except TimeoutError:
            print('error')
            return False

    async def check_paywall_in_article(self, page) -> bool:
        """
        Check is article blocked by paywall
        :param page: current browser page
        :return: Check result
        """
        try:
            await page.wait_for_selector('#barrier-page', timeout=2000)
            return True
        except TimeoutError:
            return False

    async def collect_articles_details(self, articles, page):
        print(articles)
        for article in articles:
            print(article)
            url = self.site_base_url + article.get('url')
            await page.goto(url)
            await page.wait_for_timeout(1000)

            if await self.check_paywall_in_article(page):
                logger.info(f"Paywall in '{article.get('title')}' article. Url: {url}")
                continue


    async def scrape(self):
        logger.info(f'Scraping started(First launch: {self.first_try})')
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            if not await self.check_session(page):
                return

            articles = await self.collect_articles_preliminary_information(page)
            collected_articles = await self.collect_articles_details(articles, page)
            await browser.close()

        # pprint.pprint(articles)
        return articles

# asyncio.run(Scraper('/world', first_try=False).scrape())
