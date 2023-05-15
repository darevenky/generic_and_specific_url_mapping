from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def venky1(request):
    return HttpResponse('1st view of venky')

def venky2(request):
    return HttpResponse('2nd view of app1')