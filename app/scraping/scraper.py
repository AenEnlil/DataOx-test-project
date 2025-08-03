import math
import pprint
import random
from datetime import datetime, timedelta
import asyncio
import logging
from re import sub
from typing import List, Any

from playwright.async_api import async_playwright, TimeoutError
from tzlocal import get_localzone

from settings.base import get_settings

local_tz = get_localzone()

logger = logging.getLogger('scraper')
logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)s %(message)s %(asctime)s')


class ArticleParser:

    article_date_classes = ['o-teaser__timestamp', 'stream-card__date']
    article_header_class = 'o-teaser__heading'
    article_subtitle_class = 'o-teaser__standfirst'
    article_body_selector = '#article-body'
    article_x_live_blog_class = 'article.x-live-blog-post'
    article_x_live_blog_body_class = f'div.article--body'
    article_visual_class = 'article.article-body'
    article_author_class = 'a.o3-editorial-typography-byline-author'
    article_tags_list_class = 'a.concept-list__concept'
    article_primary_tag_class = 'a.o-topper__topic'
    article_list_image_class = 'o-teaser__image-container'
    article_details_image_class = 'main-image'

    podcast_identifier_class = 'span.o-teaser__tag-suffix'

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

    async def collect_image(self, article, from_details=False):
        image_url = None
        image_div_class = self.article_list_image_class if not from_details else self.article_details_image_class
        image_div = await article.query_selector(f'div.{image_div_class}')
        if image_div:
            image = await article.query_selector('img')
            image_url = await image.get_attribute('src')
        return image_url

    async def collect_subtitle(self, article):
        subtitle_p = await article.query_selector(f'p.{self.article_subtitle_class}')
        if subtitle_p:
            text = await subtitle_p.text_content()
            return text

    async def parse_x_live_blog_article(self, page) -> dict:
        """
        Parses X live blog article type
        :param page: current page
        :return: text and word cound
        """
        article_text, word_count = '', 0
        articles_blocks = await page.query_selector_all(self.article_x_live_blog_body_class)
        articles_paragraphs = [await article.query_selector_all('p') for article in articles_blocks]
        for paragraph_block in articles_paragraphs:
            for paragraph in paragraph_block:
                text = await paragraph.text_content()
                article_text += text
                word_count += len(text.split())
        return {'content': article_text, 'word_count': word_count}

    async def parse_visual_article(self, page):
        """
        Parses visual article
        :param page: current page
        :return: text, word count
        """
        article_body = await page.query_selector(self.article_visual_class)
        paragraphs = await article_body.query_selector_all('p')
        article_text, word_count = '', 0
        for paragraph in paragraphs:
            text = await paragraph.text_content()
            article_text += text
            word_count += len(text.split())
        return {'content': article_text, 'word_count': word_count}

    async def collect_article_content(self, page) -> dict:
        """
        Collects article text from page. Logic depends on article type
        :param page: current page
        :return: text and word count
        """

        if await page.query_selector(self.article_x_live_blog_class):
            return await self.parse_x_live_blog_article(page)
        if await page.query_selector(self.article_visual_class):
            return await self.parse_visual_article(page)

        article_body = await page.query_selector(self.article_body_selector)
        article_text = await article_body.text_content()
        word_count = len(article_text.split())
        return {'content': article_text, 'word_count': word_count}

    async def collect_author(self, page) -> dict:
        author = ''
        author_data = await page.query_selector_all(f'{self.article_author_class}')
        if author_data:
            author = ', '.join([await author_tag.text_content() for author_tag in author_data])
        return {'author': author}

    async def collect_tags(self, page) -> dict:
        tags = []
        tag_list = await page.query_selector_all(f'{self.article_tags_list_class}')
        if tag_list:
            # use set to remove duplicates because tag list duplicated in html
            re_pattern = '\s+'
            tags_without_duplicates = {self.clear_text(await tag.text_content(), re_pattern) for tag in tag_list}
            tags.extend(tags_without_duplicates)
        primary_tag = await page.query_selector(f'{self.article_primary_tag_class}')
        if primary_tag:
            primary_tag_text = await primary_tag.text_content()
            if primary_tag_text not in tags:
                tags.append(primary_tag_text)
        return {'tags': tags}

    async def collect_related_articles(self, page) -> dict:
        related_articles = []
        articles_list = await page.query_selector('#onward-journey-collection')
        if articles_list:
            founded_articles = await articles_list.query_selector_all('a.js-teaser-heading-link')
            related_articles = [await article.get_attribute('href') for article in founded_articles]
        return {'related_articles': related_articles}

    async def check_if_article_should_be_skipped(self, article, skip_premium_article: bool = True) -> bool:
        """
        Skip article if it is ad, podcast or premium article(optional)
        :param article: Article to check
        :param skip_premium_article: Should premium article be skipped
        :return: Check result
        """
        skip = False
        if await article.query_selector(f'div.o-ads') or await article.query_selector('div.o-teaser--native-ad'):
            skip = True
        if await article.query_selector(f'{self.podcast_identifier_class}'):
            skip = True
        if skip_premium_article and await article.query_selector(f'span.o-labels--content-premium'):
            skip = True
        return skip

    async def parse_preliminary_information(self, article):
        if await self.check_if_article_should_be_skipped(article):
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

    async def parse_article_details(self, page, collect_image: bool) -> dict:
        collected_data = {}
        collected_content = await self.collect_article_content(page)
        collected_data.update(**collected_content)

        collected_author = await self.collect_author(page)
        collected_data.update(**collected_author)

        tags = await self.collect_tags(page)
        collected_data.update(**tags)

        related_articles = await self.collect_related_articles(page)
        collected_data.update(**related_articles)

        if collect_image:
            image_url = await self.collect_image(page, from_details=True)
            collected_data.update({'image_url': image_url})

        return collected_data

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

    @staticmethod
    def clear_text(text: str, regex_pattern: str) -> str:
        """
        Clearing text using given regex pattern
        :param text: text to clear
        :param regex_pattern: regex pattern to use
        :return: cleared text
        """
        regex = r'{0}'.format(regex_pattern)
        return sub(regex, ' ', text).strip()

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

        self.articles_per_worker = 100
        self.max_workers = 10

        self.consecutive_failures = 0

        settings = get_settings()
        self.session = settings.FTSESSION_S_COOKIE
        self.session_expires = settings.FTSESSION_S_COOKIE_EXPIRES

    async def safe_goto(self, page, url, max_retries=3, delay=2) -> bool:
        for attempt in range(1, max_retries+1):
            try:
                await page.goto(url, wait_until='load')
                return True

            except Exception as e:
                logger.warning(f'[{attempt}/{max_retries}] Failed to navigate to {url}: {e}. Retry in {delay} seconds')
                if attempt == max_retries:
                    logger.error(f'Aborting navigation to {url}')
                    return False
                await asyncio.sleep(delay)

    async def collect_articles_preliminary_information(self, page):
        """
        Collects articles information that can be accessed from articles list. Such as article url, title, subtitle,
        publication date
        :return:
        """
        articles = []
        continue_scraping = True
        logger.info('[Article list] Collecting preliminary articles information')

        while continue_scraping:
            logger.info(f'[Article list] Scraping page {self.current_page}')
            url = f'{self.url}?page={self.current_page}'
            success = await self.safe_goto(page, url)
            if not success:
                self.consecutive_failures += 1
                if self.consecutive_failures >= 5:
                    logger.error(f'[Article list] Consecutive failures limit reached. Aborting scraping')
                    break

                logger.warning(f'[Article list] Skipping page {self.current_page}')
                self.current_page += 1
                continue

            self.consecutive_failures = 0
            await page.wait_for_timeout(1000)
            parsed_articles, continue_scraping = await self.parser.parse_page(page, self.border_date)
            articles.extend(parsed_articles)

            waiting_time = random.uniform(5, 10)
            logger.info(f'[Article list] Page {self.current_page} scraped. '
                        f'Waiting {waiting_time} seconds before continue')
            await asyncio.sleep(waiting_time)

            self.current_page += 1

        logger.info(f'[Article list] Preliminary information collected. Found {len(articles)} articles')
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

    async def update_articles_with_details(self, articles, page):
        for article in articles:
            try:
                saved_url = article.get('url')
                url = self.site_base_url + saved_url if 'https' not in saved_url else saved_url
                logger.info(f"[Article details] Collecting details for '{article.get('title')}' article. Url: {url}")
                success = await self.safe_goto(page, url)
                if not success:
                    raise Exception('Failed to scrape details')
                await page.wait_for_timeout(1000)

                if await self.check_paywall_in_article(page):
                    logger.info(f"Paywall in '{article.get('title')}' article. Url: {url}")
                    continue

                collect_image = not bool(article.get('image_url'))
                article_details = await self.parser.parse_article_details(page, collect_image)
                article.update(**article_details)

                waiting_time = random.uniform(1, 3.5)
                logger.info(f"[Article details] Details of '{article.get('title')}' article collected. "
                            f"Waiting {waiting_time} seconds before continue")
                await asyncio.sleep(waiting_time)

            except Exception as e:
                waiting_time = random.uniform(1, 3.5)
                logger.error(f"[Article details] Exception {e} occurred in '{article.get('title')}' article. "
                             f"Url: {article.get('url')} "
                             f"Skipping this article in {waiting_time} seconds")
                await asyncio.sleep(waiting_time)
                continue

    @staticmethod
    def split_articles_into_batches(data: List[Any], batch_size: int) -> List[List[Any]]:
        return [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

    def calculate_articles_batch_size(self, articles_number: int) -> int:
        num_workers = min(self.max_workers, math.ceil(articles_number / self.articles_per_worker))
        batch_size = math.ceil(articles_number / num_workers)
        return batch_size

    async def scrape(self):
        cleared_articles = []
        logger.info(f'Scraping started(First launch: {self.first_try})')
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            await context.add_cookies([{"name": "FTSession_s", "value": self.session, "domain": ".ft.com", "path": "/",
                                        "expires": self.session_expires, "httpOnly": False, "secure": True,
                                        "sameSite": "Lax"}])
            page = await context.new_page()
            if not await self.check_session(page):
                return

            articles = await self.collect_articles_preliminary_information(page)

            if articles:
                batch_size = self.calculate_articles_batch_size(len(articles))
                batches = self.split_articles_into_batches(articles, batch_size)
                logger.info(f'Collecting articles details. Workers: {len(batches)}, Batch size: {batch_size}')
                tasks = [self.update_articles_with_details(batch, await context.new_page()) for batch in batches]
                await asyncio.gather(*tasks)
                logger.info('Articles details collected')
                logger.info('Clearing articles without content')
                cleared_articles = [article for article in articles if 'content' in article.keys()]
                logger.info('Articles cleared')

            await browser.close()

        return cleared_articles

# asyncio.run(Scraper('/world', first_try=False).scrape())
