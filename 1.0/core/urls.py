from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import landing_page, about_page, register_view, dashboard_view, login_view

#password reset
from .views import password_change_view

urlpatterns = [
    path('', landing_page, name='landing'),
    path('about/', about_page, name='about'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    #password reset
    path("reset-password/", password_change_view, name="reset_password"),
]
