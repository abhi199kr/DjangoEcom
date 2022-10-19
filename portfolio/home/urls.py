from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header="Abhishek"
admin.site.site_title="WElcome back"


urlpatterns = [
    
    path('home/', views.home ,name="home"),
    path('about/', views.about,name="home"),
    path('project/', views.projects,name="projects"),
    path('contact/',views.contact,name="contact")

]
