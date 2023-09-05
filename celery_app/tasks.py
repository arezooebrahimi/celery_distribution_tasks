from __future__ import absolute_import,unicode_literals
from .celery import app


@app.task(soft_time_limit=200)
def app_run_task():
    try:
        return 'ok'            
    except Exception as e:
        raise e
        