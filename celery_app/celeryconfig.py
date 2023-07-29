
broker_url='amqp://guest@localhost//'
result_backend='rpc://'
include=['celery_app.tasks']
worker_prefetch_multiplier = 1

task_routes={
    'celery_app.tasks.app_9000':{'queue':'q_9000'},
    'celery_app.tasks.app_9000':{'queue':'q_9002'},
    'celery_app.tasks.app_9000':{'queue':'q_9004'},
    'celery_app.tasks.app_9000':{'queue':'q_9006'},
    'celery_app.tasks.app_timeout':{'queue':'q_timeout'},
}
