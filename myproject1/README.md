- SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

1. run redis use file redis config
- run command: redis-server.exe redis.conf

2. run celery worker
- run command: celery -A myproject1 worker --pool=solo -l info
- add workers using the --concurrency option:
+ example: celery -A myproject1 worker --pool=solo --concurrency=4 -l info

3. run celery beat
- run command: celery -A myproject1 beat -l info