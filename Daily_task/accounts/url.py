from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name ='home'),
    path('reg/',views.reg_view,name="reg_page"),
    path('create/task',views.create_task,name="create_task"),
    path('view/task/',views.view_tasks,name="task_view"),
    path('update/task/<str:pk>',views.update_task,name="update_task"),
]
