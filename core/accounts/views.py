from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import RegisterUserForm
from django.contrib.auth import login
from django.shortcuts import redirect


class Login(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy("todo:task-list")
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('todo:task-list')
        return super().dispatch(request, *args, **kwargs)
    
class Logout(LogoutView):
     next_page = reverse_lazy('accounts:login')


class Register(FormView):
    form_class = RegisterUserForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("todo:task-list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('todo:task-list')
        return super().dispatch(request, *args, **kwargs)
    

