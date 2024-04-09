from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerRegistrationForm,DeveloperRegistrationForm
#import settings.py file for mail sending
from django.conf import settings
#send_mail is built in function in django
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from project.models import Project,UserTask
from django.shortcuts import get_object_or_404

# Create your views here.
class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerRegistrationForm
    template_name = "user/manager_register.html"
    success_url = "/user/login/"
    
    
    
class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperRegistrationForm
    template_name = "user/developer_register.html"
    success_url = "/user/login/"
    

class UserLoginView(LoginView):
    template_name = "user/login.html"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/manager_dashboard/'
            else:
                return '/user/developer_dashboard/'
            
class UserLogoutView(LogoutView):
    def get_redirect_url(self):
        if not(self.request.user.is_authenticated):
            return '/user/login/'
            
class ManagerDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        project = Project.objects.all() #select * from project
        return render(request,"user/manager_dashboard.html",{
            'project':project
        })
    
    template_name = "user/manager_dashboard.html"
    
class DeveloperDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        user_tasks = UserTask.objects.filter(user=request.user) #Filter task for the current developer
      
        return render(request,"user/developer_dashboard.html",{'user_tasks':user_tasks})
    
    template_name = "user/developer_dashboard.html"