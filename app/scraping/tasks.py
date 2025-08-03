import asyncio
import time

from datetime import datetime, timedelta
from celery import shared_task
from redis import Redis

from database.models.article import Article
from database.service import is_table_empty, bulk_insert_into_model
from settings.base import get_settings
from .scraper import Scraper

settings = get_settings()
redis = Redis.from_url(settings.CELERY_REDIS_URL)


@shared_task
def scrape_ft():
    lock_key = "scrape_ft:last_run"
    last_ts = redis.get(lock_key)

    if last_ts:
        now = datetime.utcnow()
        last_run = datetime.utcfromtimestamp(float(last_ts))
        if now - last_run < timedelta(minutes=1):
            print("[scrape_ft] Skipped duplicate run")
            return

    redis.set(lock_key, time.time())
    print("[scrape_ft] Running task")

    first_try = is_table_empty(Article)

    articles = asyncio.run(Scraper('/world', first_try=first_try).scrape())
    if articles:
        bulk_insert_into_model(Article, articles)
