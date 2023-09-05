<h2>Run celery workers</h2>
<pre>
    celery -A celery_app  worker -Q q_main --pool=solo --loglevel=INFO --concurrency=1 -n  main_worker@%h 
    celery -A celery_app  worker -Q q_start_task --pool=solo --loglevel=INFO --concurrency=4 -n  start_worker@%h 
    celery -A celery_app  worker -Q q_end_task --pool=solo --loglevel=INFO --concurrency=1 -n  end_worker@%h 
    celery flower --port=5566
    uvivorn api:app --reload
</pre>
