# ce/taks.py
# Create your tasks here
from celery import shared_task
from myproject1 import celery_app
from myproject1.celery import logger

@shared_task
def debug_task():
    logger.info("-"*25)
    logger.info("Printing Hello from Celery")
    logger.info("-"*25)