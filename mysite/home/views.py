from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("this is the data response and hello how are you?")
def school(request):
    return HttpResponse("hello school")