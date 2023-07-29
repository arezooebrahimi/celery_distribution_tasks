from __future__ import absolute_import,unicode_literals
from .celery import app
from celery.exceptions import SoftTimeLimitExceeded
from celery.app.control import Inspect
from collections import defaultdict
import time


def get_active_queue():
    try:
        i = Inspect(app=app)
        active_tasks = i.active()
        reserved_tasks = i.reserved()

        queue_stats = defaultdict(lambda: {'active': 0, 'reserved': 0})

        for worker_name, tasks in active_tasks.items():
            if 'tor' in worker_name:
                for task in tasks:
                    queue_name = task['delivery_info']['routing_key']
                    queue_stats[queue_name]['active'] += 1

        for worker_name, tasks in reserved_tasks.items():
            if 'tor' in worker_name:
                for task in tasks:
                    queue_name = task['delivery_info']['routing_key']
                    queue_stats[queue_name]['reserved'] += 1

        return dict(queue_stats)

    except Exception as e:
        raise TypeError(str(e))

def get_active_workers():
    try:
        i = Inspect(app=app)
        active_tasks = i.active()
        reserved_tasks = i.reserved()

        worker_status = {}
        if active_tasks:
            for worker_name in active_tasks:
                if 'tor' in worker_name:
                    worker_status.update({worker_name.split('@')[0]:{'active':len(active_tasks[worker_name])}})
        if reserved_tasks:
            for worker_name in reserved_tasks:
                if 'tor' in worker_name:
                    worker_status[worker_name.split('@')[0]]['reserved']=len(reserved_tasks[worker_name])

        return worker_status

    except Exception as e:
        raise TypeError(str(e))

  
@app.task(soft_time_limit=200)
def app_9000(keyword):
    inactive_app =  get_inactive_app(9000)
    if inactive_app:
        inactive_app.apply_async([keyword])
    
    else:
        try:
            # This app is supposed to do different things, 
            # the time of doing it is not known, that's why I used time.sleep()
            time.sleep(30)    
        except SoftTimeLimitExceeded as e:
            app_timeout.apply_async([keyword])
            raise e
        
    

@app.task(soft_time_limit=200)
def app_9002(keyword):
    inactive_app =  get_inactive_app(9002)
    if inactive_app:
        inactive_app.apply_async([keyword])
    
    else:
        try:
            # This app is supposed to do different things, 
            # the time of doing it is not known, that's why I used time.sleep()
            time.sleep(14)
        except SoftTimeLimitExceeded as e:
            app_timeout.apply_async([keyword])
            raise e
        

@app.task(soft_time_limit=200)
def app_9004(keyword):
    inactive_app =  get_inactive_app(9004)
    if inactive_app:
        inactive_app.apply_async([keyword])
    else:
        try:
            # This app is supposed to do different things, 
            # the time of doing it is not known, that's why I used time.sleep()
            time.sleep(50)
        except SoftTimeLimitExceeded as e:
            app_timeout.apply_async([keyword])
            raise e
   
    

@app.task(soft_time_limit=200)
def app_9006(keyword):
    inactive_app =  get_inactive_app(9004)
    if inactive_app:
        inactive_app.apply_async([keyword])

    else:
        try:
            # This app is supposed to do different things, 
            # the time of doing it is not known, that's why I used time.sleep()
            time.sleep(150)
        except SoftTimeLimitExceeded as e:
            app_timeout.apply_async([keyword])
            raise e


@app.task(soft_time_limit=400)
def app_timeout(keyword):
        try:
            # It runs when apps timeout
            time.sleep(394)        
        except SoftTimeLimitExceeded as e:
            raise e


   
app_list = [app_9000,app_9002,app_9004,app_9006]
def get_inactive_app(current_node):
    result = get_active_queue()
    queue_inactive = next((key for key, value in result.items() if value["active"] == 0), None)
    tor_node = None
    if queue_inactive:
        tor_node = int(queue_inactive.replace('q_',''))
        if tor_node == current_node:
           tor_node = None
        
        else:
            index = tor_node%9000
            if index==0:
                return app_list[0]
            else:
                return app_list[index-(index/2)]
    
    return tor_node