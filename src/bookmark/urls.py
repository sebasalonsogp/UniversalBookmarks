from django.urls import path
from . import views

urlpatterns = [
    path('bookmark/', views.bookmark, name='bookmark'),
]