from django.urls import path
from . import views



urlpatterns=[
    path("director", views.director, name='director'),
     
    
]