import asyncio
from celery import shared_task
from database.models.article import Article
from database.service import is_table_empty, bulk_insert_into_model
from .scraper import Scraper


@shared_task
def scrape_ft():
    first_try = is_table_empty(Article)

    articles = asyncio.run(Scraper('/world', first_try=first_try).scrape())
    if articles:
        bulk_insert_into_model(Article, articles)
