import email
from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.
class product(models.Model):
    proudctid=models.AutoField
    pname=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=60,default="")
    price=models.IntegerField(default=0)
    des=models.CharField(max_length=200)
    pub_date=models.DateField()
    img=models.ImageField(upload_to="static/shop",default='')
    def __str__(self):
        return self.pname
class Contact(models.Model):
    id=models.AutoField
    fname=models.CharField(max_length=50,default="a")
    email=models.EmailField(max_length=60,default="")
    phone=models.IntegerField(default=0)
    des=models.TextField(max_length=200)
    # def __str__(self):
    #     return self.fname
class Orders(models.Model):
    orderid=models.AutoField(primary_key=True)
    itemsjson=models.CharField(max_length=5000)
    name=models.CharField(max_length=50)
   


    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipc=models.CharField(max_length=50)
class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)
    def __str__(self):
        return self.update_desc[0:7] + "..."
class myuser(models.Model):
    userid=models.CharField(max_length=50,unique=False)
    email=models.EmailField(max_length=100)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    
    
    
  