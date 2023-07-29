from fastapi import FastAPI, HTTPException,Request
from celery_app.tasks import app_1000,app_1002,app_1004,app_1006,get_active_queue
import random

app = FastAPI()


@app.get("/run_tasks")
async def run_tasks(num_of_tasks:int):
    try: 
        app_list = [app_1000,app_1002,app_1004,app_1006]

        for i in range(0,num_of_tasks, 4):
            app_list[0].apply_async() 
            app_list[1].apply_async()     
            app_list[2].apply_async()     
            app_list[3].apply_async()     
    
        
        return 'ok'

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/get_active_queue")
async def get_active_q():
    res = get_active_queue()
    print(res)
    return 'ok'
