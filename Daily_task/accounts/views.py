from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required(login_url='login_page')
def home(request):
    return render(request, 'accounts/main.html')


# def reg_view(request):
#     registration_form = reg_form()
#     if request.method == 'POST':
#         registration_form = reg_form(request.POST)
#         if registration_form.is_valid():
#             registration_form.save()
#             message = "User Successfully Registered."
#             messages.success(request,message)
#             return redirect('task_view')
#         else:
#             message = "User Registration Failed."
#             messages.error(request,message)
#             return redirect('reg_page')
#     context = {'form_table':registration_form}
#     return render(request,'accounts/registration.html',context)

def reg_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = reg_form()
        if request.method == 'POST':
            form = reg_form(request.POST)
            if form.is_valid():
                form.save()
                print("User saved")
                user = form.cleaned_data.get('username')
                messages.success(request, "Account created for "+user)
                return redirect('login_page')
            else:
                print("User failed to register.")
                messages.error(request, "User creation failed. ")
                return redirect('reg_page')
        context = {'form': form}
        return render(request, 'accounts/registration.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('task_view')
            else:
                messages.error(request,"Username or password is incorrect.")
                return render(request, 'accounts/login.html')
        return render(request, 'accounts/login.html')

@login_required(login_url='login_page')
def logout_user(request):
    logout(request)
    return redirect('login_page')

@login_required(login_url='login_page')
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
            messages.error(request, message)
            print("It must be Fail")
            return redirect('create_task')
    context = {'form_table': created_form}
    # print("It must be succes")
    return render(request, 'accounts/create_task.html', context)

@login_required(login_url='login_page')
def view_tasks(request):
    task = tasks.objects.all().order_by('priority')
    if task.count() == 0:
        print("No tasks are there. Please create to see.")
        return render(request, 'accounts/zerotask_page.html')
    else:
        myfilter = taskfilter(request.GET, queryset=task)
        task = myfilter.qs
        context = {"tasks": task, 'myfilter': myfilter}
        return render(request, 'accounts/tasks.html', context)

@login_required(login_url='login_page')
def update_task(request, pk):
    task = tasks.objects.get(id=pk)
    form = task_form(instance=task)  # task_form is the name of the form.
    if request.method == 'POST':
        form = task_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_view')
    context = {'form_table': form}
    return render(request, 'accounts/create_task.html', context)

@login_required(login_url='login_page')
def delete_task(request, pk):
    task = tasks.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('task_view')
    context = {'task': task}
    return render(request, 'accounts/confirm_delete_task.html', context)
