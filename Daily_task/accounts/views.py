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
            return redirect('task_view')
        else:
            message = "User Registration Failed."
            messages.error(request,message)
            return redirect('home')
    context = {'form_table':registration_form}
    return render(request,'accounts/registration.html',context)

def create_task(request):
    created_form = task_form()
    if request.method == 'POST':
        created_form = task_form(request.POST)
        if created_form.is_valid():
            created_form.save()
            message = "Task has been created Successfully."
            messages.success(request, message)
            print("It must be succes")
            return redirect('task_view')
        else:
            message = "Task Creation Failed."
            messages.error(request,message)
            print("It must be Fail")
            return redirect('create_task')
    context = {'form_table':created_form}
    #print("It must be succes")
    return render(request,'accounts/create_task.html',context)

def view_tasks(request):
    task = tasks.objects.all().order_by('priority')
    context = {"tasks":task}
    return render(request,'accounts/tasks.html',context)

def update_task(request,pk):
    task = tasks.objects.get(id=pk)
    form = task_form(instance=task)               #task_form is the name of the form.
    if request.method == 'POST':
        form = task_form(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_view')
    context = {'form_table':form}
    return render(request,'accounts/create_task.html',context)

def delete_task(request,pk):
    task = tasks.objects.get(id=pk)
    task.delete()
    return render(request,'accounts/confirm_delete_task.html')

