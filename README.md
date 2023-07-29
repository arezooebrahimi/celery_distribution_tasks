
celery -A celery_app  worker -Q q_1000--loglevel=INFO --concurrency=1 -n  worker_1000@%h
celery -A celery_app  worker -Q q_1002 --loglevel=INFO --concurrency=1 -n worker_1002@%h
celery -A celery_app  worker -Q q_1004 --loglevel=INFO --concurrency=1 -n worker_1004@%h
celery -A celery_app  worker -Q q_1006 --loglevel=INFO --concurrency=1 -n worker_1006@%h
celery -A celery_app  worker -Q q_timeout --loglevel=INFO --concurrency=1 -n timeout@%h
