from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('', views.bookmark, name='bookmark'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]