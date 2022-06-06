from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
context={"name":"Abhishek","language":"Django"}
def home(request):
    return render(request,"home.html",context)
def about(request):
    return render(request,'about.html',context)
def projects(request):
    return render(request,'project.html',context)
def contact(request):
    return render(request,'contact.html',context)