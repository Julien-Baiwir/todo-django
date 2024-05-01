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
    

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'  
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    contex_object_name ='task'
    template_name = "base/task.html"
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class DeleteView(LoginRequiredMixin, DeleteView): 
    model = Task
    contex_object_name ='task'
    success_url = reverse_lazy('tasks')
    