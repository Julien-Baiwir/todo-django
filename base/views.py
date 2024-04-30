from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']  


from .models import Task



class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        success_url = reverse_lazy('tasks')
        print(f"Redirecting to: {success_url}")  # Add this line
        return success_url
    

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    contex_object_name ='tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context



class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    contex_object_name ='task'
    template_name = "base/task.html"
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class DeleteView(LoginRequiredMixin, DeleteView): 
    model = Task
    contex_object_name ='task'
    success_url = reverse_lazy('tasks')
    