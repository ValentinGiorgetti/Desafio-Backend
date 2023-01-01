import os
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FriendsLessonsSystem.settings')

from django.conf import settings

app = Celery("FriendsLessonsAPI")
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'add-every-10-minutes' : {
        'task' : 'send_notification_email',
        'schedule' : crontab(minute='*/10')
    }
}