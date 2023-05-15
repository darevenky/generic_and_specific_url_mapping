from django.urls import path
from app1.views import *
app_name='something'

urlpatterns=[
    path('venky1/',venky1,name='venky1'),
    path('venky2/',venky2,name='venky2'),
]