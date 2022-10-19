from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from bloghome.models import Blog

# Create your views here.
def home(request):
    return render(request,"index.html")
def blog(request):
    blogs=Blog.objects.all()
    context={"allblog":blogs}
    return render(request,"bloghome.html",context)
def search(request):
    return render(request,"search.html")
def contact(request):
    return render(request,"contact.html")
def blogpost(request, slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={"blog":blog}
    return render(request,"blogpost.html",context)