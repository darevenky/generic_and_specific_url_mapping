from app2.views import *
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('venkydare1/',venkydare1,name='venkydare1'),
    path('venkydare2/',venkydare2,name='venkydare2'),
]