from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloworldfunc(request):
    print(request)
    return HttpResponse('hello world')