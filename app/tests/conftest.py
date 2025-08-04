import pytest
import pytest_asyncio

from playwright.async_api import async_playwright

# related articles always will be empty in test, because downloaded html's don`t have them
article_details_fields = ['content', 'word_count', 'author', 'tags', 'related_articles']


@pytest_asyncio.fixture()
async def playwright_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()

