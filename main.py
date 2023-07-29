from fastapi import FastAPI, HTTPException
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel
from celery_app.tasks import app_9000,app_9002,app_9004,app_9006
import random

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000) # For GZIP


class RunTaskItem(BaseModel):
    num_of_keywords:int


app.post("/run_tasks")
async def run_tasks(item:RunTaskItem):
    try: 
        app_list = [app_9000,app_9002,app_9004,app_9006]
        keywords = []
        for i in range(item.num_of_keywords):
            keywords.append(random.choice(open("keywords.txt" , encoding='utf-8').readlines()))

        for i in range(0,len(keywords), 4):
            batch = keywords[i:i+4]
            for j in range(4):
                app_list[j].apply_async([batch[j].replace("\n", ""),0])     
        
        return 'ok'

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
