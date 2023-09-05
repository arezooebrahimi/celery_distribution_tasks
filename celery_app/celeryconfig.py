
broker_url='amqp://guest@localhost//'
result_backend='rpc://'
include=['celery_app.tasks']
broker_connection_retry_on_startup=True
from celery.schedules import crontab

beat_schedule = {
 'run-every-day-at-12': {
    'task': 'celery_app.tasks.app_run_task',
    # 'schedule': crontab(hour=9, minute=0),
    'schedule': crontab(hour=17, minute=5),
    'args': ([], 'fa'),
 }
}

task_routes={
    'celery_app.app_run_task':{'queue':'q_main'}
}
