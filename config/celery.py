import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTING_MODULE', 'config.settings')

app = Celery('mailape')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
