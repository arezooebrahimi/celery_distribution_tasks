<h2>Run celery workers</h2>
<pre>
    celery -A celery_app  worker -Q q_main --loglevel=INFO --concurrency=10 -n  worker@%h 
    celery flower --port=5566
    uvivorn api:app --reload
</pre>
