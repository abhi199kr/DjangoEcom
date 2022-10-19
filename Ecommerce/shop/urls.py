from django.contrib import admin
from django.urls import path,include
from shop import views
urlpatterns = [
  
    path("",views.index,name="index"),
    path("about/",views.about,name="about"), 
    path("contact/",views.contact,name="contact"),
    path("search/",views.search,name="search"),
    path("checkout/",views.checkout,name="checkout"),
    path("productview/<int:myid>",views.productview,name="procuctdetail"),
    path("tracker/",views.tracker,name="tracker"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
]