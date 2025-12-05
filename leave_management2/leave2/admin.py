from django.contrib import admin
from .models import *
class Employee_registration(admin.ModelAdmin):
    list_display=["id","profile_pic","first_name","middle_name","last_name","department","gender","email","contact", "username","password","age","date","work_time","break_time","work_status","work_date","clockin_time","clockout_time","work_hours",]
admin.site.register(Employee,Employee_registration)


class Tasks_adding(admin.ModelAdmin):
    list_display=["employee","email","a","b","c","d","e","f","g","h","i","date"]
admin.site.register(Tasks,Tasks_adding)

class Department_adding(admin.ModelAdmin):
    list_display=["shortname","fullname","date",]
admin.site.register(Department,Department_adding)

class leave_adding(admin.ModelAdmin):
    list_display=["leave","Description","date",]
admin.site.register(Leaves_Table,leave_adding)

class Leave_adding(admin.ModelAdmin):
    list_display=["email","id","name","leave_type","start_date","end_date","half_day","joining_date","reason","status","count","leave_count","approve_count","pending_count","deny_count"]
admin.site.register(Leave,Leave_adding)

class TimeEntry_d(admin.ModelAdmin):
    list_display=["date_field","clockin_time1","clockin_time2","email","Break_in","Break_out",]
admin.site.register(TimeEntry,TimeEntry_d)

class Clock_a(admin.ModelAdmin):
    list_display=["date","email","clockin_time","clockout_time","work_hours","break_time","work_time",]
admin.site.register(Clock,Clock_a)



class ClockEventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'timestamp')
    list_filter = ('event_type', 'timestamp')
    search_fields = ('event_type',)
    ordering = ('-timestamp',)

admin.site.register(ClockEvent, ClockEventAdmin)

from django.contrib import admin
from .models import Timer

@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    list_display = ('clock_in_time', 'clock_out_time', 'break_in_time', 'break_out_time', 'total_work_time', 'total_break_time')
    list_filter = ('clock_in_time', 'clock_out_time')
    search_fields = ['clock_in_time', 'clock_out_time']



