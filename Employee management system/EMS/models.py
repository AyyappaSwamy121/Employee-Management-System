from django.db import models
from datetime import date

class Employee(models.Model):
    id=models.IntegerField(null=False,primary_key=True)
    profile_pic = models.ImageField(upload_to='task_images/')
    first_name=models.CharField(max_length=200)
    middle_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    email=models.EmailField(null=True)
    contact=models.IntegerField(null=True)
    username=models.CharField(max_length=200, default="none")
    password=models.IntegerField(null=True,default="0")
    age=models.IntegerField(null=True,default=" 0")
    date=models.DateField()
    work_time=models.TimeField(default="00:00:00")
    break_time=models.TimeField(default="00:00:00")
    work_status=models.IntegerField(null=True,default="0")
    work_date=models.DateField(null=True)
    clockin_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    clockout_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    work_hours = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
 
    
class Tasks(models.Model):
    employee=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    a=models.CharField(max_length=200)
    b=models.CharField(max_length=200)
    c=models.CharField(max_length=200)
    d=models.CharField(max_length=200)
    e=models.CharField(max_length=200)
    f=models.CharField(max_length=200)
    g=models.CharField(max_length=200)
    h=models.CharField(max_length=200)
    i=models.CharField(max_length=200,default="none")
    date=models.DateField(auto_now=True)

class Department(models.Model):
    shortname=models.CharField(max_length=50)
    fullname=models.CharField(max_length=50)
    date = models.DateField(default=date.today)
 

class Leaves_Table(models.Model):
    leave=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)


class Leave(models.Model):
    email=models.EmailField(null=True)
    id=models.IntegerField(null=False,primary_key=True)
    name=models.CharField(max_length=20)
    leave_type=models.CharField(max_length=50)
    start_date=models.DateField(default="null")
    end_date=models.DateField(default="null")
    half_day=models.CharField(max_length=20)
    joining_date=models.DateField(default="null")
    reason=models.CharField(max_length=200)
    status=models.IntegerField(null=True ,default="0")
    count=models.IntegerField(null=True ,default="0")
    count=models.IntegerField(null=True,default="0")
    leave_count=models.IntegerField(null=True,default="0")
    approve_count=models.IntegerField(null=True,default="0")
    pending_count=models.IntegerField(null=True,default="0")
    deny_count=models.IntegerField(null=True,default="0")
    







class ClockEvent(models.Model):
    CLOCK_IN = 'IN'
    CLOCK_OUT = 'OUT'
    BREAK_IN = 'BREAK_IN'
    BREAK_OUT = 'BREAK_OUT'
    
    EVENT_CHOICES = [
        (CLOCK_IN, 'Clock In'),
        (CLOCK_OUT, 'Clock Out'),
        (BREAK_IN, 'Break In'),
        (BREAK_OUT, 'Break Out'),
    ]
    
    event_type = models.CharField(max_length=10, choices=EVENT_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_event_type_display()} at {self.timestamp}"
    

# models.py

from django.db import models

class Timer(models.Model):
    clock_in_time = models.DateTimeField(auto_now_add=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)
    break_in_time = models.DateTimeField(null=True, blank=True)
    break_out_time = models.DateTimeField(null=True, blank=True)
    total_work_time = models.IntegerField(default=0)  # in seconds
    total_break_time = models.IntegerField(default=0)  # in seconds

class TimeEntry(models.Model):

    email=models.EmailField(null=True)
    date_field=models.DateField(default=date.today)
    clockin_time1 = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    clockin_time2 = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Break_in = models.TimeField(null=True)
    Break_out = models.TimeField(null=True)


class Clock(models.Model):
    email=models.EmailField(null=True)
    date=models.DateField(auto_now=True)
    clockin_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    clockout_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    work_hours = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    break_time=models.TimeField(default="00:00:00")
    work_time=models.TimeField(default="00:00:00")

 

    