from django.urls import path, request, render
from . import views

urlpatterns=[
        path('', views.index, name='home'),

]
