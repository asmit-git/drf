from django.urls import path

from . import views

# Explicit imports 
# from .views import api_home

urlpatterns = [
    path('',views.api_home)
]