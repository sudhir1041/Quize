from django.shortcuts import render,redirect,HttpResponse
import re

# Create your views here.
def home(request):
    return render(request,'index.html')
def registration(request):
    return render(request,'registration.html')


def students_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email == '':
            msg = 'Please enter an email id'
            return render(request, 'login.html', {'error': msg})
        elif password == '':
            msg = 'Please enter a password'
            return render(request, 'login.html', {'error': msg})
        elif not re.match(r'^[\w\.-]+@[\w\.-]+(\.[\w]+)+$', email):
            msg = 'Please enter a valid email address'
            return render(request, 'login.html', {'error': msg})
        else:  
            if len(password) < 8:
                msg = 'Password must be at least 8 characters long'
                return render(request, 'login.html', {'error': msg})
            else:
                pass
        
def teacher_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email == '':
            msg = 'Please enter an email id'
            return render(request, 'login.html', {'error': msg})
        elif password == '':
            msg = 'Please enter a password'
            return render(request, 'login.html', {'error': msg})
        elif not re.match(r'^[\w\.-]+@[\w\.-]+(\.[\w]+)+$', email):
            msg = 'Please enter a valid email address'
            return render(request, 'login.html', {'error': msg})
        else:  
            if len(password) < 8:
                msg = 'Password must be at least 8 characters long'
                return render(request, 'login.html', {'error': msg})
            else:
                pass
def students_dashboard(request):
    return render(request,'student_dashboard.html')
def teacher_dashboard(request):
    return render(request,'teacher_dashboard.html')
