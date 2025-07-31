import asyncio
from celery import shared_task
from database.models.article import Article
from database.service import is_table_empty
from .scraper import Scraper


@shared_task
def scrape_ft():
   first_try = is_table_empty(Article)

   articles = asyncio.run(Scraper('/world', first_try=first_try).scrape())

   # articles = await Scraper('/world', first_try=True).scrape()

   # from pprint import pprint
   # pprint(articles)
