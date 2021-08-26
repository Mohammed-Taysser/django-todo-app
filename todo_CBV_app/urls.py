from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('add/', views.AddTask.as_view(), name='add_task'),
    path('update/<int:pk>', views.UpdateTask.as_view(), name='update_task'),
    path('delete/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
    path('update-task-completeness/<int:task_id>',
         views.update_task_completeness, name='update_task_completeness'),
]
