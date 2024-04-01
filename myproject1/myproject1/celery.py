#cmd: celery -A your_app_name worker --pool=solo -l info
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
import logging

logger = logging.getLogger("Celery")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("log.txt")
logger.addHandler(handler)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject1.settings')

app = Celery('myproject1')

app.config_from_object('django.conf:settings', namespace='CELERY')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks([
    'products',
    'customer',
    'user_devices',
    'tokens',
    'connect',
    'database',
    'device',
    'error',
    'FTP_Server',
    'memory',
    'relay',
    'sensor',
    'thiet_bi'
    ])

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

#     # Calls test('hello') every 30 seconds.
#     # It uses the same signature of previous task, an explicit name is
#     # defined to avoid this task replacing the previous one defined.
#     sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)

#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )

# @app.task(bind=True)
# def test(arg):
#     print(arg)

# @app.task(bind=True, name="debug-task")
# def debug_task():
#     logger.info("-"*25)
#     logger.info("Printing Hello from Celery")
#     logger.info("-"*25)
