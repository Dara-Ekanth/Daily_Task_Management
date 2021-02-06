from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'accounts/main.html')
def reg_view(request):
    registration_form = reg_form()
    if request.method == 'POST':
        registration_form = reg_form(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            message = "User Successfully Registered."
            messages.success(request,message)
            return redirect('home')
        else:
            message = "User Registration Failed."
            messages.error(request,message)
            return redirect('home')
    context = {'form_table':registration_form}
    return render(request,'accounts/registration.html',context)

def create_task(request):
    task_forms = task_form()
    if request.method == 'POST':
        task_forms = task_form(request.POST)
        if task_forms.is_valid():
            task_forms.save()
            message = "Task has been created Successfully."
            messages.success(request, message)
            print("It must be succes")
            return redirect('home')
        else:
            message = "Task Creation Failed."
            messages.error(request,message)
            print("It must be Fail")
            return redirect('create_task')
    context = {'form_table':task_forms}
    print("It must be succes")
    return render(request,'accounts/create_task.html',context)