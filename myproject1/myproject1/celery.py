#cmd: celery worker -A myproject --pool=solo worker -l info
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

app = Celery('myproject1')#, include="myproject1.celery")#, broker="redis://localhost")
# app.conf.update(
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Europe/Oslo',
#     enable_utc=True,
# )
# app.conf.broker_url     = 'redis://localhost:6379/0'
# app.conf.beat_schedule = {
#     'debug-task': {
#         'task': 'myproject1.celery.debug_task',
#         'schedule': crontab(minute='*/1'),
#         # 'args': (16, 16)
#     },
# }
# app.conf.timezone = 'UTC'
# app.conf.result_backend = 'redis://localhost:6379/0'
app.config_from_object('django.conf:settings', namespace='CELERY')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(['products'])

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
