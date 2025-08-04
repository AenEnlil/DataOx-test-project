import asyncio
import datetime
import zoneinfo
from pathlib import Path

import pytest

from scraping.scraper import ArticleParser
from tests.conftest import article_details_fields
from tests.parsing_examples import default_article_details, default_article_image_url, visual_investigation_article, \
    list_article_pub_date, list_article_link_and_title, list_article_subtitle, first_list_article_preliminary_information


# details parsing related tests


async def test_parsing_details_of_default_article(playwright_page):
    html_path = Path("tests/html/default_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().parse_article_details(playwright_page, collect_image=False)
    assert parsed_data

    keys = parsed_data.keys()
    for field in article_details_fields:
        assert field in keys
        if field != 'tags':
            assert parsed_data.get(field) == default_article_details.get(field)

    default_article_tags = default_article_details.get('tags')
    for tag in parsed_data.get('tags'):
        assert tag in default_article_tags


async def test_parsing_details_of_default_article_with_image(playwright_page):
    html_path = Path("tests/html/default_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().parse_article_details(playwright_page, collect_image=True)
    assert parsed_data

    keys = parsed_data.keys()
    for field in article_details_fields:
        assert field in keys
        if field != 'tags':
            assert parsed_data.get(field) == default_article_details.get(field)

    default_article_tags = default_article_details.get('tags')
    for tag in parsed_data.get('tags'):
        assert tag in default_article_tags

    assert 'image_url' in keys
    image_url = parsed_data.get('image_url')
    assert image_url
    assert image_url == default_article_image_url


async def test_collect_article_content_for_default_article(playwright_page):
    html_path = Path("tests/html/default_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().collect_article_content(playwright_page)
    assert parsed_data

    assert parsed_data.get('content') == default_article_details.get('content')
    assert parsed_data.get('word_count') == default_article_details.get('word_count')


async def test_collect_author_for_default_article(playwright_page):
    html_path = Path("tests/html/default_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().collect_author(playwright_page)
    assert parsed_data

    assert parsed_data.get('author') == default_article_details.get('author')


async def test_collect_tags_for_default_article(playwright_page):
    html_path = Path("tests/html/default_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().collect_tags(playwright_page)
    assert parsed_data

    tags = parsed_data.get('tags')
    default_article_tags = default_article_details.get('tags')
    for tag in tags:
        assert tag in default_article_tags


async def test_collect_related_articles_for_default_article(playwright_page):
    html_path = Path("tests/html/default_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().collect_related_articles(playwright_page)
    assert parsed_data

    related_articles = parsed_data.get('related_articles')
    default_article_related_articles = default_article_details.get('related_articles')
    assert related_articles == default_article_related_articles


async def test_parse_visual_article(playwright_page):
    html_path = Path("tests/html/visual_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().parse_visual_article(playwright_page)
    assert parsed_data

    assert parsed_data.get('content') == visual_investigation_article.get('content')
    assert parsed_data.get('word_count') == visual_investigation_article.get('word_count')


async def test_collect_article_content_for_visual_article(playwright_page):
    html_path = Path("tests/html/visual_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().collect_article_content(playwright_page)
    assert parsed_data

    assert parsed_data.get('content') == visual_investigation_article.get('content')
    assert parsed_data.get('word_count') == visual_investigation_article.get('word_count')


async def test_parsing_details_of_visual_article(playwright_page):
    html_path = Path("tests/html/visual_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().parse_article_details(playwright_page, collect_image=False)
    assert parsed_data

    keys = parsed_data.keys()
    for field in article_details_fields:
        assert field in keys
        if field != 'tags':
            assert parsed_data.get(field) == visual_investigation_article.get(field)


async def test_collect_image_from_details(playwright_page):
    html_path = Path("tests/html/default_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().collect_image(playwright_page, from_details=True)
    assert parsed_data
    assert parsed_data == default_article_image_url


# preliminary data collection related test

async def test_collect_date_from_list_article(playwright_page):
    html_path = Path("tests/html/list_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_date = await ArticleParser().collect_publication_date(playwright_page)
    assert parsed_date
    assert str(parsed_date) == list_article_pub_date


async def test_collect_link_and_title_from_list_article(playwright_page):
    html_path = Path("tests/html/list_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().collect_link_and_title(playwright_page)
    assert parsed_data
    assert parsed_data == list_article_link_and_title


async def test_collect_subtitle_from_list_article(playwright_page):
    html_path = Path("tests/html/list_article.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    parsed_data = await ArticleParser().collect_subtitle(playwright_page)
    assert parsed_data
    assert parsed_data.strip() == list_article_subtitle


async def test_check_if_article_should_be_skipped(playwright_page):
    html_path = Path("tests/html/world_page_1.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    articles_skipped = False
    articles_list = await playwright_page.query_selector('ul.o-teaser-collection__list')
    articles = await articles_list.query_selector_all('li')

    for article in articles:
        skipping = await ArticleParser().check_if_article_should_be_skipped(article)
        if skipping and not articles_skipped:
            articles_skipped = True

    assert articles_skipped


async def test_parse_preliminary_information_from_articles_list(playwright_page):
    html_path = Path("tests/html/world_page_1.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    articles_list = await playwright_page.query_selector('ul.o-teaser-collection__list')
    articles = await articles_list.query_selector_all('li')

    parsed_data = await ArticleParser().parse_preliminary_information(articles[0])
    assert parsed_data

    for key in first_list_article_preliminary_information:
        assert parsed_data.get(key) == first_list_article_preliminary_information.get(key)

    assert parsed_data.get('scraped_at')


async def test_parse_list_page_with_stop_scraping(playwright_page):
    html_path = Path("tests/html/world_page_1.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    border_date = datetime.datetime(2025, 8, 3, 21, 19, 58, tzinfo=zoneinfo.ZoneInfo(key='Europe/Kyiv'))
    parsed_articles, continue_scraping = await ArticleParser().parse_page(playwright_page, border_date)
    assert parsed_articles
    assert not continue_scraping


async def test_parse_list_page_with_continue_scraping(playwright_page):
    html_path = Path("tests/html/world_page_1.html")
    html_content = html_path.read_text(encoding='utf-8')
    await playwright_page.set_content(html_content)

    border_date = datetime.datetime(2025, 8, 1, 21, 19, 58, tzinfo=zoneinfo.ZoneInfo(key='Europe/Kyiv'))
    parsed_articles, continue_scraping = await ArticleParser().parse_page(playwright_page, border_date)
    assert parsed_articles
    assert continue_scraping

