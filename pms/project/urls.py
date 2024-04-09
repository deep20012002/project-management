from django.contrib import admin
from .views import *
from django.urls import path,include
from . import views

urlpatterns = [
    path("create/",ProjectCreationView.as_view(),name="project_create"),
    path("list/",ProjectListView.as_view(),name="project_list"),
    path("create_team/",ProjectTeamCreateView.as_view(),name="project_team_create"),
    path("view_team/<int:id>",views.project_team_view,name="project_team_view"),
    path("update/<int:pk>",ProjectUpdateview.as_view(),name="update_project"),
    path("detail/<int:pk>/",ProjectDetailView.as_view(),name="detail_project"),
    path("delete/<int:id>",views.delete_project,name="delete_project"),
    
    path("create_module/",ModuleCreationView.as_view(),name="module_create"),
    path("list_module/",ModuleListView.as_view(),name="module_list"),
    path("update_module/<int:pk>",ModuleUpdateview.as_view(),name="module_update"),
    path("detail_module/<int:pk>/",ModuleDetailView.as_view(),name="module_detail"),
    path("delete_module/<int:id>",views.delete_module,name="module_delete"),
    
    path("create_task/",TaskCreationView.as_view(),name="task_create"),
    path("list_task/",TaskListView.as_view(),name="task_list"),
    path("update_task/<int:pk>",TaskUpdateview.as_view(),name="task_update"),
    path("detail_task/<int:pk>/",TaskDetailView.as_view(),name="task_detail"),
    path("delete_task/<int:id>",views.delete_task,name="task_delete"),
    
    path("task_assign/",TaskAssignView.as_view(),name="task_assign"),
]