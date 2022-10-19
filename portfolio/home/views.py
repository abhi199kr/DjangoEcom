from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from home import models
# Create your views here.
context={"name":"Abhishek","language":"Django"}
def home(request):
    return render(request,"home.html",context)
def about(request):
    return render(request,'about.html',context)
def projects(request):
    return render(request,'project.html',context)
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        lastname=request.POST['lastname']
       # phone=request.POST['phone']
        message=request.POST['message']
        
        print("This is post")
        print(name,email,lastname,message)
        ins=models.contact(name=name,email=email,lastname=lastname)
        ins.save()
        print("the data has been written to the database")
    return render(request,'contact.html',context)