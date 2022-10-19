from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from home.models import task
# Create your views here.
def home(request):
    context={'success': False,'name':'Abhishek'}
    if request.method=="POST":
        #handle the form
        title=request.POST["title"]
        titledes=request.POST["titledes"]
        print(title,titledes)
        ins = task(tasktitle=title,taskdes=titledes)
        ins.save()
       
    #return HttpResponse ("hellow Abhihsek")
    return render(request,"index.html",context)
def Task(request):
    
    #alltask.objects.all()
    alltask=task.objects.all()
    # for item in alltask:
    #     print(item.taskdes)
    # print(alltask)
  
    
    context={"tasks":alltask}
    return render(request,"task.html",context)