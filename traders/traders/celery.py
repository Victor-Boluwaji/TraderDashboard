import os
from celery import Celery

#default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traders.settings')

#new Celery instance
app = Celery('traders')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks
app.autodiscover_tasks()
