from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
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
@unauthenticated_user
def reg_view(request):
    form = reg_form()
    if request.method == 'POST':
        form = reg_form(request.POST)
        b = beneficiare()
        if form.is_valid():
            user1=form.save()
            # b.name = form.cleaned_data.get('username')
            # b.save()
            print("User saved")
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user1.groups.add(group)
            beneficiare.objects.create(user=user1)
            messages.success(request, "Account created for "+username)
            return redirect('login_page')
        else:
            print("User failed to register.")
            messages.error(request, "User creation failed. ")
            return redirect('reg_page')
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)

@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            # print("the id of the user is",request.user.id)
            context = {'id':request.user.id}
            return redirect('home')
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
    user_name = request.user.beneficiare
    print("The name of the user in the create task is",request.user)
    created_form = task_form()
    print("the user is ",request.user)
    print("The title is",request.POST.get('title'))
    # data = {
    #     'title': request.POST.get('title'),
    #     'date_created': request.POST.get('title'),
    #     'days_to_do': request.POST.get('title'),
    #     'deadline': request.POST.get('title'),
    #     'description': request.POST.get('title'),
    #     'priority': request.POST.get('title'),
    #     'user': user_name,
    # }
    #created_form['user'] = 'user_name'
    #print(created_form)
    if request.method == 'POST':
        created_form = task_form(request.POST)
        if created_form.is_valid():
            created_form.save()
            lastrow = tasks.objects.all().last()
            #print("The top row  is",toprow)
            # tasktitle = tasks.objects.get(title=toprow.title)
            # print("The title got from the tasks query is",tasktitle)
            buser= beneficiare.objects.get(user=request.user)
            print("The user from the buser is",buser)
            lastrow.user = buser
            lastrow.save()

            print("The cleaned get is",created_form.cleaned_data.get('user'))
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
#@allowed_users(allowed_roles=['admin','user'])
def view_tasks(request):
    print("the id of the user is", request.user.id)
    #task = tasks.objects.filter(user=request.user).order_by('priority')
    task = request.user.beneficiare.tasks_set.all().order_by('priority')
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

def settings_view(request):
    userr = request.user.beneficiare
    form = settigs_form(instance=userr)
    if request.method == 'POST':
        form = settigs_form(request.POST,request.FILES,instance=userr)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'accounts/accounts_settings.html',context)
