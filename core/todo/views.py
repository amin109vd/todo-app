from django.shortcuts import render
from django.views.generic import ListView, CreateView ,DetailView, UpdateView, DeleteView
from . models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count() 
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'

class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description']
    success_url = reverse_lazy('todo:task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class UpdateTask(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description']
    success_url = reverse_lazy('todo:task-list')

class ToggleTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['complete']

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise PermissionError("you don't have permission for change this")
        return task

    def form_valid(self, form):
        task = form.save(commit=False)
        task.complete = 'complete' in self.request.POST
        task.user = self.request.user
        task.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')



class DeleteTask(LoginRequiredMixin,DeleteView):
     model = Task
     success_url = reverse_lazy('todo:task-list')