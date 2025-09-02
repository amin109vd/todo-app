from django.urls import path
from .views import *

app_name = 'todo'

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('task-detail/<int-pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', CreateTask.as_view(), name='task-create'),
    path('task/<int-pk>/update/', UpdateTask.as_view(), name='task-update'),
    path('task-/<int-pk>/delete', DeleteTask.as_view(), name='task-delete'),
]