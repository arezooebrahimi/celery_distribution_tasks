<h2>Run celery workers</h2>
<pre>
celery -A celery_app  worker -Q q_app --loglevel=INFO --concurrency=4 -n  worker_1000@%h 
celery -A celery_app  worker -Q q_timeout --loglevel=INFO --concurrency=1 -n timeout@%h   
</pre>
