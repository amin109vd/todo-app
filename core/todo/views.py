from django.shortcuts import render
from django.views.generic import ListView, CreateView ,DetailView, UpdateView, DeleteView
from . models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'

class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class UpdateTask(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description']
    success_url = reverse_lazy('todo:task-list')

class DeleteTask(LoginRequiredMixin,DeleteView):
     model = Task
     success_url = reverse_lazy('todo:task-list')