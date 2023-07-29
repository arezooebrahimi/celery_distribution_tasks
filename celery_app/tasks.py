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
            for task in tasks:
                queue_name = task['delivery_info']['routing_key']
                queue_stats[queue_name]['active'] += 1

        for worker_name, tasks in reserved_tasks.items():
            for task in tasks:
                queue_name = task['delivery_info']['routing_key']
                queue_stats[queue_name]['reserved'] += 1

        return dict(queue_stats)

    except Exception as e:
        raise TypeError(str(e))

  
@app.task(soft_time_limit=200)
def app_1000():
    inactive_app =  get_inactive_app(1000)
    if inactive_app:
        inactive_app.apply_async()
    
    else:
        try:
            # The running time of apps (app_1000, app_1002, app_1004, app_1006) is different, I used sleep for simulation
            time.sleep(30)    
        except SoftTimeLimitExceeded as e:
            app_timeout.apply_async()
            raise e
        
    

@app.task(soft_time_limit=200)
def app_1002():
    inactive_app =  get_inactive_app(1002)
    if inactive_app:
        inactive_app.apply_async()
    
    else:
        try:
            # The running time of apps (app_1000, app_1002, app_1004, app_1006) is different, I used sleep for simulation
            time.sleep(14)
        except SoftTimeLimitExceeded as e:
            app_timeout.apply_async()
            raise e
        

@app.task(soft_time_limit=200)
def app_1004():
    inactive_app =  get_inactive_app(1004)
    if inactive_app:
        inactive_app.apply_async()
    else:
        try:
            # The running time of apps (app_1000, app_1002, app_1004, app_1006) is different, I used sleep for simulation
            time.sleep(50)
        except SoftTimeLimitExceeded as e:
            app_timeout.apply_async()
            raise e
   
    

@app.task(soft_time_limit=200)
def app_1006():
    inactive_app =  get_inactive_app(1004)
    if inactive_app:
        inactive_app.apply_async()

    else:
        try:
            # The running time of apps (app_1000, app_1002, app_1004, app_1006) is different, I used sleep for simulation
            time.sleep(150)
        except SoftTimeLimitExceeded as e:
            app_timeout.apply_async()
            raise e


@app.task(soft_time_limit=400)
def app_timeout():
        try:
            # It runs when apps timeout
            time.sleep(394)        
        except SoftTimeLimitExceeded as e:
            raise e


   
app_list = [app_1000,app_1002,app_1004,app_1006]
def get_inactive_app(current_node):
    print(f'run get_inactive_app c={current_node}')
    result = get_active_queue()
    queue_inactive = next((key for key, value in result.items() if value["active"] == 0), None)
    print(f'run get_inactive_app inactive={queue_inactive}')

    tor_node = None
    if queue_inactive:
        tor_node = int(queue_inactive.replace('q_',''))
        if tor_node == current_node:
           tor_node = None
        
        else:
            index = tor_node%1000
            if index==0:
                return app_list[0]
            else:
                return app_list[index-(index/2)]
    
    return tor_node