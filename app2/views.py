from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def venkydare1(request):
    return HttpResponse('1st view of app2')

def venkydare2(request):
    return HttpResponse('2nd view of app2')