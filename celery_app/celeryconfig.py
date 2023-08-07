
broker_url='amqp://guest@localhost//'
result_backend='rpc://'
include=['celery_app.tasks']
worker_prefetch_multiplier = 1

task_routes={
    'celery_app.tasks.app_1000':{'queue':'q_app'},
    'celery_app.tasks.app_1002':{'queue':'q_app'},
    'celery_app.tasks.app_1004':{'queue':'q_app'},
    'celery_app.tasks.app_1006':{'queue':'q_app'},
}
