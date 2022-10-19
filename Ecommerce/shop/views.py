import email
import json
from math import ceil
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import product,Contact,Orders,OrderUpdate,myuser
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    products=product.objects.all()
    print(product)
    # n=len(products)
    # nslide=n//4 + ceil((n/4)-(n//4))
    # params={'product':products,'slide':nslide,'range':range(1,nslide)}
    # allProds=[[products, range(1, nslide), nslide],[products, range(1, nslide), nslide]]
    # For categories wise
    allProds=[]
    catprods= product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n = len(prod)
        nslide = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nslide), nslide])
    params={'allProds':allProds }
    return render(request,"shop/index.html",params)
def about(request):
    return render(request,"shop/about.html")
def contact(request):
    thank=False
    if request.method =='POST':
        print(request)
        fname=request.POST.get('name', '')
        
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        des=request.POST.get('message', 'ab')
        print(fname,email,phone)
        con=Contact(fname=fname,email=email,phone=phone,des=des)
        con.save()
        thank=True
        
    return render(request,"shop/contact.html" , {'thank':thank})
def search(request):
    return HttpResponse("This is searcht section of shop")
def productview(request,myid):
    products=product.objects.filter(id=myid)
    return render(request,"shop/productview.html",{'prodcut':products[0]})
def checkout(request):
    return render(request,"shop/checkout.html")
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(orderid=orderId,email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].itemsjson], default=str)
                    
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,"shop/tracker.html")
def checkout(request):
    if request.method =='POST':
        print(request)
        itemsjson= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
    
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        zipc=request.POST.get('zipc', 'ab')
        state=request.POST.get('state', 'ab')
        city=request.POST.get('city', 'ab')
        
        print(name,email,phone)
        
        ord=Orders(itemsjson=itemsjson,name=name,email=email,phone=phone,state=state,city=city,zipc=zipc,)
        ord.save()
        update= OrderUpdate(order_id= ord.orderid, update_desc="The order has been placed")
        update.save()
        thank = True
        id = ord.orderid
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')
def login(request):
    
    return render(request,"shop/login.html")
def signup(request):
    # if request.method=='post':
    #     # Get the post parameters
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('/shop/')
    
    return render(request,"shop/signup.html")
    
# paytm checkout
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})