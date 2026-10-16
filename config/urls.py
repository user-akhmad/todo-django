"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/', views.about, name='about'),
    path('tasks/', views.task_list, name="task_list"),
    path('tasks/done/', views.done, name='done'),
    path('tasks/active/', views.active, name='active'),
    path('tasks/<int:task_id>/delete', views.task_delete, name='task_delete'),
    path('tasks/<int:task_id>/done/', views.task_done, name='task_done'),
    path('api/tasks/', views.api_task_list, name='api_task_list'),
]
