from django.urls import path
from about import views

urlpatterns = [
    path('', views.register, name='register'),
    path('home', views.register, name='home')
] 