from __future__ import absolute_import,unicode_literals
from .celery import app
from celery.exceptions import SoftTimeLimitExceeded
from celery.app.control import Inspect
from collections import defaultdict
import time

  
@app.task(soft_time_limit=200)
def app_1000():
    try:
        # The running time of apps (app_1000, app_1002, app_1004, app_1006) is different, I used sleep for simulation
        time.sleep(30)    
    except SoftTimeLimitExceeded as e:
        raise e
        
    

@app.task(soft_time_limit=200)
def app_1002():
    try:
        # The running time of apps (app_1000, app_1002, app_1004, app_1006) is different, I used sleep for simulation
        time.sleep(14)
    except SoftTimeLimitExceeded as e:
        raise e
        

@app.task(soft_time_limit=200)
def app_1004():
    try:
        # The running time of apps (app_1000, app_1002, app_1004, app_1006) is different, I used sleep for simulation
        time.sleep(50)
    except SoftTimeLimitExceeded as e:
        raise e
   
    

@app.task(soft_time_limit=200)
def app_1006():
    try:
        # The running time of apps (app_1000, app_1002, app_1004, app_1006) is different, I used sleep for simulation
        time.sleep(150)
    except SoftTimeLimitExceeded as e:
        raise e
