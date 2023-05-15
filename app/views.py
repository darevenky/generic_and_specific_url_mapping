from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def venkydare(request):
    return HttpResponse('this is 1st project')

def venky(request):
    return HttpResponse('this is 2nd view')
