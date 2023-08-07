<h2>Run celery workers</h2>
<pre>
    celery -A celery_app  worker -Q q_app --loglevel=INFO --concurrency=4 -n  worker@%h 
    celery flower --port=5566
    uvivorn api:app --reload
</pre>
