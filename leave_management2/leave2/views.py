from django.shortcuts import render,redirect
from django.contrib.auth import  logout,login
from django.http import *
from .models import *
from django.core.mail import send_mail
from django.contrib import messages

def member(request):
    return HttpResponse("HELLO WORLD")

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
def Admin_Login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                if user.is_active and user.is_staff:
                    login(request, user)
                    
                    return redirect('admin_dashboard')   
                else:
                    login(request, user)
                    return redirect('user_dashboard')
            else:
                return redirect("password_validate")
        else:
             return redirect("email_validate")
    return render(request, 'home.html')

def User_Login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        request.session['email'] = email
        
        if Employee.objects.filter(email=email).exists():
            member = Employee.objects.get(email=email)
            p= int(password)
            if member.password == p:
              
               
                otp = generate_otp()
                print(otp)
                request.session['otp'] = otp
                send_mail(
                     'Your OTP',
                     f'Your OTP is : {otp}',
                     'from@example.com',
                     [email],
                     fail_silently=False,
                 )
                return redirect('validate_otp')
                
            else:
                 return redirect("password_validate")
        else:
            return redirect("email_validate")

    return render(request, 'home.html')

from .utils import *
def send_otp(request):
    if request.method == 'POST':
            email = request.session.get('email')
            otp = generate_otp()
            request.session['otp'] = otp
            send_mail(
                'Your OTP',
                f'Your OTP is : {otp}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return redirect('validate_otp')
    return render(request,'otp.html')

def validate_otp(request):
    if request.method == 'POST':
        entered_otp=request.POST.get("entered_otp")
        stored_otp = request.session.get('otp')
        print(stored_otp)
        print(entered_otp)
        if stored_otp and entered_otp == stored_otp: 
            return redirect("employee")
        else:
            return redirect("otp_invalid")
    return render(request,'otp.html')
    

  



def index(request):
    return render(request,"home.html")

def aaa(request):
    return render(request,"aaa.html")

def index(request):
    return render(request,"home.html")

def employee_add_success(request):
    return render(request,"employee_add_success.html")

def employee_history(request):
    task3=Employee.objects.all()
    context={
        'task3':task3,
    }
    return render(request,"employee_history.html",context)

def admin_dashboard(request):
    task=Leave.objects.all()
    count =task.filter(status=0).count()
    task3=Employee.objects.all()
    count =task.filter(status=0).count()
    task=Leave.objects.all()
    
    count =task.filter(status=0).count()
    approved=0
    pending=0
    denied=0
    for x in task:
        if x.status == 1:
            approved+=1
        elif x.status == 2:
            denied+=1
        elif x.status == 3:
            pending+=1
        else:
            print("none")
    emp=0
    for x in task3:
        emp+=1
    context={
        'task':task,
        'task3':task3,
        'count':count,
        'approved':approved,
        'pending':pending,
        'denied':denied,
        'emp':emp,
    }
    print(task)
    emp=0
    for x in task3:
        emp+=1
        
    return render(request,"index.html",context)

def user_dashboard(request):
    
    return render(request,"employee.html")


def employee(request):
    email = request.session.get('email')
    print(email)
    taskz=Leave.objects.filter(email=email)
    task=Employee.objects.get(email=email)
    print(taskz)
    context={
        'taskz':taskz,
        'task':task,
    }
    return render(request,"employee.html",context)

def email_validate(request):
    return render(request,"email_validate.html")

def password_validate(request):
    return render(request,"password_validate.html")

def password_success(request):
    return render(request,"password_success.html")

def password_alert(request):
    return render(request,"password_alert.html")

def pass_con_alert(request):
    return render(request,"pass_con_alert.html")

def password_validate(request):
    return render(request,"password_validate.html")

def email_validate(request):
    return render(request,"email_validate.html")


def add_employee(request):
    task=Department.objects.all()
    context={
        'task':task,
    }
    return render(request,"add_employee.html",context)

def manage_employee(request):
    return render(request,"manage_employee.html")

def add_leave_type(request):
    return render(request,"add_leave_type.html")

def manage_leave_type(request):
    return render(request,"manage_leave_type.html")

def all_leave(request):
    return render(request,"all_leave.html")

def pending_leave(request):
    return render(request,"pending_leave.html")

def approve_leave(request):
    return render(request,"approve_leave.html")

def not_approve_leave(request):
    return render(request,"not_approve_leave.html")

def add_user(request):
    return render(request,"add_user.html")

def manage_user(request):
    return render(request,"manage_user.html")

def leave_success(request):
    return render(request,"leave_success.html")


def apply_leave(request):
    email = request.session.get('email')
    task= Employee.objects.get(email=email)
    task2= Leaves_Table.objects.all().values()
    print(task)
    context={
        'task':task,
        'task2':task2,
    }
    return render(request,"apply_leave.html",context)

def leave_status(request):
    return render(request,"leave_status.html")


def leave_apply_success(request):
    return render(request,"leave_apply_success.html")

def otp_invalid(request):
    return render(request,"otp_invalid.html")

def website(request):
    return render(request,"Arsha/index2.html")
def clock(request):
    email = request.session.get('email')
    if Employee.objects.filter(email=email, work_date=date.today()).exists():
            return redirect('work_time')
    else:
        task= Employee.objects.get(email=email)
        task2=TimeEntry.objects.filter(email=email)
        print(task)
        context={
        'task':task,
        'task2':task2,
        }
        return render(request,"clock.html",context)

def work_time(request):
     email = request.session.get('email')

     task= Employee.objects.get(email=email)





     task2= TimeEntry.objects.filter(email=email,date_field=date.today())
     task3= Clock.objects.get(email=email,date=date.today())
    
     print(task)
     context={
     'task':task,
     'task2':task2,
     'task3':task3,
     }
     return render(request,"work_time.html",context)

def works(request):
     email = request.session.get('email')
     if Tasks.objects.filter(email=email, date=date.today()).exists():
            return redirect("show_tasks")
     else:
        task= Employee.objects.get(email=email)
        print(task)
        context={
        'task':task,
     }
     return render(request,"works.html",context)

def manage_department(request):
    return render(request,"manage_department.html")

def add_department(request):
    return render(request,"add_department.html")

def success_update(request):
    return render(request,"success_update.html")

def employee_success(request):
    return render(request,"employee_success.html")

def delete_alert(request):
    return render(request,"delete_alert.html")

def delete_alert2(request):
    return render(request,"delete_alert2.html")

def department_success(request):
    return render(request,"department_success.html")

def employee_work(request):
    return render(request,"employee_work.html")

def works_success(request):
    return render(request,"works_success.html")

def employee_delete_alert(request):
    return render(request,"employee_delete_alert.html")

def work_duplicate_alert(request):
    return render(request,"work_duplicate_alert.html")

def profile_update_success(request):
    return render(request,"profile_update_success.html")

def work_duplicate_alert(request):
    return render(request,"work_duplicate_alert.html")

def department_duplicate(request):
    return render(request,"department_duplicate.html")

def leave_update_success(request):
    return render(request,"leave_update_success.html")



def registration(request):
          
        if request.method == "POST":
            profile_pic = request.FILES.get('profile_pic')
            if profile_pic:
                print("success")
            else:
                print("error")
                
            first_name = request.POST.get('first_name')
            id = request.POST.get('id')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            gender = request.POST.get('gender')
            date = request.POST.get('date')
            age = request.POST.get('age')
            department = request.POST.get('department')
            contact = request.POST.get('contact')

            print(password)
            if Employee.objects.filter(email=email).exists() or User.objects.filter(email=email):
                return HttpResponse("Email  already exists")
            if Employee.objects.filter(id=id).exists():
                return HttpResponse("id  already exists")
            
            else:
                user = Employee(profile_pic=profile_pic, id=id,middle_name=middle_name,first_name = first_name,last_name = last_name,email = email,contact=contact,username = username, password=password,age=age, gender=gender,date=date,department=department)
                user.save()
                send_mail(
                            'Login Details ',
                            'Your email is ::' + email + ' your password is::'+password,
                            'subhashvelugula1299@gmail.com',
                            [email],
                            fail_silently=False,
                     )

        return redirect("employee_add_success")

from datetime import date

def tasks(request):
    
     
      if request.method == "POST":
         a = request.POST.get('a')
         b = request.POST.get('b')
         c = request.POST.get('c')
         d = request.POST.get('d')
         e = request.POST.get('e')
         f = request.POST.get('f')
         g = request.POST.get('g')
         h = request.POST.get('h')
         i = request.POST.get('i')
         email = request.session.get('email')
         print(email)     
         # Retrieve employee
         employee = Employee.objects.get(email=email)
         employee2 = Employee.objects.filter(email=email).values()
         emp_date = employee.date  # Assuming 'date' is a field in your Employee mode     
         print(emp_date)
         print(date.today())
         print(employee)
         print(employee2)
         # Check if employee has already submitted data for today
         if Tasks.objects.filter(email=email, date=date.today()).exists():
             return redirect("show_tasks")
         else:
             username = employee.username
             print(username)
             user = Tasks(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, date=emp_date, employee=username, email=email)
             user.save()
             return redirect('works_success')
      return render(request, 'works.html')




def show_tasks(request):
    email = request.session.get('email')
    print(email)
    task2=Tasks.objects.filter(email=email)
    task=Employee.objects.get(email=email)
    
    context={
            'task2':task2,
            'task':task,
    }
    print(task)
    return render(request,"show_tasks.html",context)



        
def department(request):
    if request.method == "POST":
        shortname=request.POST.get('shortname')
        fullname=request.POST.get('fullname')
        if Department.objects.filter(shortname=shortname).exists():
            return redirect("department_duplicate")
        else:
            user= Department(shortname=shortname,fullname=fullname)
            user.save()
            return redirect('department_success')
    return render(request,'add_department.html')

        
def leave_adding(request):
    if request.method == "POST":
        leave=request.POST.get('leave')
        Description=request.POST.get('Description')
        if Leaves_Table.objects.filter(leave=leave).exists():
            # return redirect("department_duplicate")
            return HttpResponse("duplicate")
        else:
            user= Leaves_Table(leave=leave,Description=Description)
            user.save()
            return redirect('leave_success')
    return render(request,'add_leave_type.html')

def show_departments(request):
    task=Department.objects.all().values()
    context={
        'task':task,
    }
    return render(request,"manage_department.html",context)

def show_leaves_types(request):
    task=Leaves_Table.objects.all().values()
    context={
        'task':task,
    }
    return render(request,"manage_leave_type.html",context)

def show_pendings(request):
    task=Leave.objects.all().values()
    context={
        'task':task,
    }
    return render(request,"pending_leave.html",context)

def show_employees(request):
    task=Employee.objects.all()
    context={
        'task':task,
    }
    return render(request,"manage_employee.html",context)

def show_approved(request):
    task=Leave.objects.all().values()
    context={
        'task':task,
    }
    return render(request,"approve_leave.html",context)

def show_not_approved(request):
    task=Leave.objects.all().values()
    context={
        'task':task,
    }
    return render(request,"not_approve_leave.html",context)

def show_leave_status(request):
    email = request.session.get('email')
    task2=Leave.objects.filter(email=email)
    task=Employee.objects.get(email=email)
    print(task)
    context={
        'task':task,
        'task2':task2,
    }
    return render(request,"leave_status.html",context)

def leave_history(request):
    email = request.session.get('email')
    task2=Leave.objects.filter(email=email)
    task=Employee.objects.get(email=email)
    print(task)
    context={
        'task':task,
        'task2':task2,
    }
    return render(request,"leave_history.html",context)


def show_employee(request):
    if request.method == "POST":
        date=request.POST.get("date")
        print(date)
        task=Tasks.objects.filter(date=date)
        # print(task)
        context={
        'task':task,
        }
        print(task)
        return render(request,"employee_table.html",context)
    
    return render(request,"employee_table.html",context)






def update_task1(request, pk):
    task2 = Department.objects.get(id=pk)
    task=Leave.objects.all().values()
    print(task2)
    if request.method == 'POST':
        
        task2.shortname = request.POST.get('shortname')
        task2.fullname = request.POST.get('fullname')
        print(task2)
        task2.save()
        return redirect("success_update")
    context = {
        'task2': task2,  
        'task': task  
    }
    return render(request, 'update_task.html', context)

def update_leave(request, pk):
    task2 = Leaves_Table.objects.get(id=pk)
    task = Leave.objects.all().values()
    if request.method == 'POST':
        
        task2.leave = request.POST.get('leave')
        task2.Description = request.POST.get('Description')
        task2.save()
        return redirect("leave_update_success")
    context = {
        'task2': task2,
        'task': task,
    }
    return render(request, 'update_leave.html', context)

def deleteTask1(request, pk):
    item = Department.objects.get(id=pk)
    request.session["item_pk"] = pk  # Store the primary key instead of the object itself
    if item is not None:
        return redirect("delete_alert")
    return render(request, 'manage_department.html')

def a(request):
    pk = request.session.get("item_pk")
    if pk is not None:
        try:
            item = Department.objects.get(id=pk)
            item.delete()
            del request.session["item_pk"]  # Delete the stored primary key from session after deletion
            return redirect("show_departments")
        except Department.DoesNotExist:
            pass
    return HttpResponse("error")

from django.http import JsonResponse




def delete_leave(request,pk):
    item = Leaves_Table.objects.get(id=pk)
    request.session["item_pk"] = pk
    if item is not None:
        return redirect("delete_alert2")
    return render(request,'manage_leave_type.html')


def leave_alert(request):
    pk = request.session.get("item_pk")
    if pk is not None:
        try:
            item = Leaves_Table.objects.get(id=pk)
            item.delete()
            del request.session["item_pk"] 
            return redirect("show_leaves_types")
        except Department.DoesNotExist:
            pass
    return HttpResponse("error")



def delete_employee(request,pk):
    item = Employee.objects.get(id=pk)
    request.session["item_pk"] = pk
    print(item)
    if item is not None:
        return redirect("employee_delete_alert")
    return render(request,'manage_employee.html')



def employee_alert(request):
    pk = request.session.get("item_pk")
    if pk is not None:
        try:
            item = Employee.objects.get(id=pk)
            item.delete()
            del request.session["item_pk"] 
            return redirect("show_employees")
        except Department.DoesNotExist:
            pass
    return HttpResponse("error")



def update_employee(request, pk):
    task2 = Employee.objects.get(id=pk)
    task = Employee.objects.all().values()
    task3=Department.objects.all()
    print(task2.email)
    request.session['task.email']=task2.email
    if request.method == 'POST':
            # task2.profile_pic = request.FILES.get('profile_pic')
            task2.first_name = request.POST.get('first_name')
            task2.id = request.POST.get('id')
            task2.middle_name = request.POST.get('middle_name')
            task2.last_name = request.POST.get('last_name')
            task2.email = request.POST.get('email')
            email2 = task2.email 
            task2.username = request.POST.get('username')
            task2.password = request.POST.get('password')
            task2.gender = request.POST.get('gender')
            task2.age = request.POST.get('age')
            task2.contact = request.POST.get('contact')
            task2.department = request.POST.get('department')
            task2.save()
            print(email2)
            print(task2.email)
            email=request.session.get("task.email")
            print(email)
            if Leave.objects.filter(email=email):
                Leave.objects.filter(email=email).update(email=task2.email)

            if Tasks.objects.filter(email=email).exists():
                Tasks.objects.filter(email=email).update(email=task2.email)

            if Clock.objects.filter(email=email).exists():
                Clock.objects.filter(email=email).update(email=task2.email)

            if TimeEntry.objects.filter(email=email).exists():
                TimeEntry.objects.filter(email=email).update(email=task2.email)
            return redirect("employee_success")
    context = {
        'task2': task2,
        'task': task,
        'task3': task3,
    }
    return render(request, 'update_employee.html', context)


def update_profile(request):
    email = request.session.get('email')
    task=Employee.objects.get(email=email)
    if request.method == 'POST':
        task.profile_pic = request.FILES.get('profile_pic')
        task.save()
        return redirect("profile_update_success")
    context={
        'task':task
    }
    return render(request, 'update_profile.html', context)




def apply(request):
    if request.method == "POST":
        leave_type = request.POST.get("leave_type")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        half_day = request.POST.get("half_day")
        joining_date = request.POST.get("joining_date")
        reason = request.POST.get("reason")
        email = request.session.get('email')

        if Employee.objects.filter(email=email).exists():
                member = Employee.objects.get(email=email)
                username = member.username

            
                # If no leave record exists, create a new one
                Leave.objects.create(
                    leave_type=leave_type,
                    start_date=start_date,
                    end_date=end_date,
                    half_day=half_day,
                    joining_date=joining_date,
                    reason=reason,
                    name=username,
                    email=email
                )
                return redirect("leave_apply_success")
        
    return render(request, "apply_leave.html")




def show_leaves(request):
    task=Leave.objects.all().values()
    context={
        'task':task,
    }
    return render(request,"all_leave.html",context)

def approve(request,pk):
    member =Leave.objects.get(id=pk)
    if member.status == 3:
        member.pending_count -=1
    member.status =1
    member.save()
    member.count+=1
    member.save()
    member.approve_count+=1
    member.save()
    email=member.email
    send_mail(
            'Leave Approval',
            'Your leave has been  approved ....',
            'subhashvelugula1299@gmail.com',
            [email],
            fail_silently=False,
            )
    return redirect('show_leaves')

def reject(request,pk): 
    member =Leave.objects.get(id=pk)
    if member.status == 3:
        member.pending_count -=1
    member.status =2
    member.save()
    member.deny_count+=1
    member.save()
    email=member.email
    send_mail(
            'Leave Denied',
            'Your leave is not approved..',
            'subhashvelugula1299@gmail.com',
            [email],
            fail_silently=False,
            )
    return redirect('show_leaves')

def pending(request,pk):
    member =Leave.objects.get(id=pk)
    member.status =3
    member.save()
    member.pending_count+=1
    member.save()
    email=member.email
    send_mail(
            'Pending....🔃',
            'Your leave is on hold ... wait for while',
            'subhashvelugula1299@gmail.com',
            [email],
            fail_silently=False,
            )
    return redirect('show_leaves')


def notifications(request):
    task=Leave.objects.all().values()
    count = tasks.filter(status=0).count()
    print(task)
    context={
        'task':task,
        'count':count
    }
    return render(request,"sidebar.html",context)

def show_sidebar(request):
    task=Leave.objects.all().values()
    # print(task)
    context={
        'task':task,
       
    }
    return render(request,"base.html",context)

# views.py

from datetime import datetime, timedelta
from django.shortcuts import redirect, HttpResponse
from .models import Employee

from datetime import datetime, timedelta
from django.shortcuts import redirect, HttpResponse
from .models import Employee
from datetime import datetime
from datetime import datetime
from django.shortcuts import redirect, HttpResponse
from .models import Employee

from datetime import datetime, timedelta
from django.shortcuts import redirect, HttpResponse
from .models import Employee

def save_time(request):
    email = request.session.get('email')
    if request.method == 'POST':
        if Employee.objects.filter(email=email).exists():
            member = Employee.objects.get(email=email)
            clock_in_time = request.POST.get('clock_in_time')
            break_time = request.POST.get('break_time')
           
            member.work_time = clock_in_time
            member.break_time = break_time
            member.work_status = 3
            member.save()

            # Get the current time
            now = datetime.now()
            formatted_now = now.strftime("%H:%M:%S")
            member.clockout_time = formatted_now
            member.work_date = datetime.today()
            if Clock.objects.filter(email=email,date=date.today()).exists():
                member2=Clock.objects.get(email=email,date=date.today())
                print(member)
                member2.clockout_time = formatted_now
                member2.break_time = break_time
                member2.work_time = clock_in_time
                member2.save()

            # Get the clock-in time from session
            formatted_now2 = request.session.get('formatted_now2')

            if formatted_now2 is not None and isinstance(formatted_now2, str):
                # Convert string times to datetime objects
                time_format = "%H:%M:%S"
                time1 = datetime.strptime(formatted_now, time_format)
                time2 = datetime.strptime(formatted_now2, time_format)

                # Calculate time difference
                time_difference = time1 - time2

                # Format time difference as HH:MM[:ss[.uuuuuu]]
                formatted_difference = str(time_difference)

                # Save formatted time difference as total hours
                member.work_hours = formatted_difference

                member.save()
                if Clock.objects.filter(email=email,date=date.today()).exists():
                    member3=Clock.objects.get(email=email,date=date.today())
                    print(member)
                    member3.work_hours = formatted_difference
                    member3.save()
            else:
                return HttpResponse("Clock-in time not found or invalid format in session.")
            
            return redirect("clock")
        else:
            return HttpResponse("Employee not found.")
    else:
        return HttpResponse('Invalid request method.')
    

from datetime import datetime
def save_time2(request, timer=None):
    email = request.session.get('email')
    if request.method == 'POST':
        if Employee.objects.filter(email=email, work_date=date.today()).exists():
            return HttpResponse("work is already submitted")
        else:
            if Employee.objects.filter(email=email).exists():
                 member = Employee.objects.get(email=email)
                 member2=TimeEntry.objects.filter(email=email)
                 print(member2)
                 member.work_status = 1
                 member.save()
                 member.work_date=date.today()
                 member.save()
                 now = datetime.now()
                 formatted_now2 = now.strftime("%H:%M:%S")
                 request.session['formatted_now2'] = formatted_now2
                 request.session.save()
                 formatted_now2 = request.session.get('formatted_now2')
                 print( "sdf",formatted_now2)
                 print("formated::",formatted_now2)
                 for x in member2:
                    x.clockin_time1=formatted_now2
                    x.save()
                 member.clockin_time= formatted_now2
                 Clock.objects.create(
                    clockin_time= formatted_now2,
                    date=date.today(),
                    email=email
                )
                 member.save()
                 
                 timer = 'clockIn'
                 return redirect('clock',timer)
            else:
                return HttpResponse('Invalid request method.')
def employee_status(request):
    task= Employee.objects.filter(work_date=date.today())
    # task= Employee.objects.all().values()
    task2= TimeEntry.objects.all().values()
    task3= Clock.objects.filter(date=date.today()).values()
    print(task3)
    
    print(task)
    context={
        'task':task,
        'task2':task2,
        'task3':task3,
    }
    return render(request,"employee_status.html",context)

def update_password(request):
    email = request.session.get('email')
    email = request.session.get('email')
    task= Employee.objects.get(email=email)
    context={
        'task':task,
    }
    if request.method == 'POST':
        old_pass = request.POST.get("old_pass")
        new_pass = request.POST.get("new_pass")
        con_pass = request.POST.get("con_pass")
        old_pass=int(old_pass)
        if new_pass == con_pass:
            if Employee.objects.filter(email=email).exists():
                member = Employee.objects.get(email=email)
                if member.password == old_pass:
                    member.password=new_pass
                    member.save()
                    return redirect("password_success")
                else:
                   return redirect("password_alert")
        else:
            return redirect("pass_con_alert")
    return render(request, "update_password.html",context)
            
def report(request):
    task=Leave.objects.all()
    
    count =task.filter(status=0).count()
    approved=0
    pending=0
    denied=0
    for x in task:
        if x.status == 1:
            approved+=1
        elif x.status == 2:
            denied+=1
        elif x.status == 3:
            pending+=1
        else:
            print("none")
        
    context={
        'approved':approved,
        'pending':pending,
        'denied':denied,
        'count':count,
    }
    print(approved)
    print(pending)
    print(denied)
    return render(request,"reports.html",context)        




        

from django.utils import timezone


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
@csrf_exempt
def save_time_to_database(request):
    if request.method == 'POST':
        time_type = request.POST.get('timeType')
        email = request.session.get('email', 'default@example.com')  # default email if not in session
        now = datetime.now()
        formatted_now = now.strftime("%H:%M:%S")

        # Get the latest TimeEntry object for the current user from today
        today = datetime.now().date()
        latest_entry = TimeEntry.objects.filter(email=email, date_field=today).order_by('-id').first()

        if time_type == 'clockIn':
            # This case is straightforward: always create a new entry for clockIn
            TimeEntry.objects.create(email=email, clockin_time1=formatted_now, date_field=today)

        elif time_type == 'break':
            if latest_entry:
                # Assuming only one break per session for simplicity
                latest_entry.Break_in = formatted_now
                latest_entry.clockin_time2 = formatted_now
                latest_entry.save()

        elif time_type == 'continue':
            if latest_entry and latest_entry.Break_in and not latest_entry.Break_out:
                # If there is a Break_in without a corresponding Break_out, update Break_out
                latest_entry.Break_out = formatted_now
                latest_entry.save()
                # And then create a new entry to mark the continuation of work
                TimeEntry.objects.create(email=email, clockin_time1=formatted_now, date_field=today)

        elif time_type == 'clockOut':
            if latest_entry and not latest_entry.clockin_time2:
                # Only update clockin_time2 if it hasn't been set yet
                latest_entry.clockin_time2 = formatted_now
                latest_entry.save()

        return JsonResponse({'status': 'success'})

    else:
        return JsonResponse({'status': 'error'}, status=400)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import TimeEntry  

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import TimeEntry  # Assuming you have a TimeEntry model defined in your models.py


def history(request,email):
    task=Employee.objects.filter(email=email).values()
    request.session["email2"]=email
    print(task)
    print(email)
    
    return redirect("display_entries_by_month")



from django.shortcuts import render
from datetime import datetime

def display_entries_by_month(request):
    if request.method == 'POST':
        selected_month = request.POST.get('selectedMonth')
        email = request.session.get('email2')
        email2 = request.session.get('email')
        print(email2)
        print(email)
        task= Employee.objects.all().filter(email=email)
        clock= Clock.objects.all().filter(email=email)
        print(task)
        try:
            month = datetime.strptime(selected_month, '%Y-%m')
            time_entries = TimeEntry.objects.filter(email=email, date_field__year=month.year, date_field__month=month.month)
            time_entries = time_entries.order_by('date_field')
            return render(request, 'display_entries.html', {'time_entries': time_entries,'task': task,'clock':clock})
        except ValueError:
            # Handle invalid date format
            return render(request, 'display_entries.html', {'error': 'Invalid date format'})
    else:
        # Handle GET request
        return render(request, 'display_entries.html')
