from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name ='home'),
    path('reg/',views.reg_view,name="reg_page"),
    path('login/',views.login_view,name="login_page"),
    path('logout/',views.logout_user,name='logout'),
    path('create/task',views.create_task,name="create_task"),
    path('view/task/',views.view_tasks,name="task_view"),
    path('update/task/<str:pk>',views.update_task,name="update_task"),
    path('delete/task/<str:pk>',views.delete_task,name="delete_task"),
    path('settings/',views.settings_view,name='settings'),
]
