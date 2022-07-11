import datetime
from time import time 
from plyer import notification
from scheduler import Scheduler
Task = input("Type your task: ")
hourse = float(input("The hourse you want to remdainer be ur task: "))
minutie = float(input("The minutie you want to remdainer be ur task: "))

def todo():
    notification.notify(
            title = "TODO",
            message= Task ,
           
            # displaying time
            timeout=10
)
schedule = Scheduler()
schedule.cyclic(datetime.timedelta(dayes,hourse,minutie,), todo)


