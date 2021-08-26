from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.add_task, name='add_task'),
    path('update-task/<int:task_id>', views.update_task, name='update_task'),
    path('delete-task/<int:task_id>', views.delete_task, name='delete_task'),
    path('update-task-completeness/<int:task_id>',
         views.update_task_completeness, name='update_task_completeness'),
]
