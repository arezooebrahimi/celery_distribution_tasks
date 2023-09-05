from fastapi import FastAPI, HTTPException
from celery_app.tasks import app_run_task
app = FastAPI()


@app.get("/run_tasks")
async def run_tasks():
    try: 
        app_run_task.apply_async() 
        return 'ok'

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    