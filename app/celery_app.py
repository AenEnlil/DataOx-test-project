import os
import sys

from database.db import init_db
from celery import Celery
from celery.signals import worker_ready
from settings.base import get_settings

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
settings = get_settings()

app = Celery('celery', broker=settings.CELERY_REDIS_URL)
app.autodiscover_tasks(['app.scraping'])

app.conf.timezone = 'UTC'
app.conf.beat_schedule = {
    'scrape-every-60-minutes': {
        'task': 'app.scraping.tasks.scrape_ft',
        'schedule': 60*60.0,  # 60 minutes
        'args': (),
    },
}


@worker_ready.connect
def startup_task(sender, **kwargs):
    init_db()
    sender.app.send_task('app.scraping.tasks.scrape_ft')
