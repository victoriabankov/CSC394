"""
URL configuration for site1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import redirect
from dashpage.views import dashboard, create_todo, delete_todo, start_todo, pause_todo, stop_todo, edit_todo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('dashboard')),
    path('dashboard/', dashboard, name='dashboard'),
    path('todos/create/', create_todo, name='create_todo'),
    path('edit/<int:todo_id>/', edit_todo, name='edit_todo'),
    path('todos/delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('todos/start/<int:todo_id>/', start_todo, name='start_todo'),
    path('todos/<int:id>/pause/', pause_todo, name='pause_todo'),
    path('todos/<int:id>/stop/', stop_todo, name='stop_todo')

]

