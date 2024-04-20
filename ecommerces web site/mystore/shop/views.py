from django.shortcuts import render
from django.http import HttpResponse
from .models import product,contact,order,orderupdate
from math import ceil
import json

# Create your views here.
# Products = product.objects.all()
def index(request):
    
    allproducts = []
    catprods = product.objects.values('category','id')
    categorys = {item['category'] for item in catprods}
    for cat in categorys:
        prodt = product.objects.filter(category = cat)  
        n = len(prodt)
        SlideNo = n//4+ceil((n/4)-(n//4)) 
        allproducts.append([prodt,range(1,SlideNo),SlideNo])

    # prams = {'no_of_slides':SlideNo,'range':range(SlideNo+1),'product':Products}
    prams = {'allproducts':allproducts}
    return render(request,'shop/index.html',prams)

def about(request):
    return render(request,'shop/about.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contacts = contact(name = name , email = email , phone = phone , desc = desc)
        contacts.save()
    return render(request,'shop/contact.html')

def track(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            Orders = order.objects.filter(order_id=orderId, email=email)
            if len(Orders)>0:
                update = orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def search(request):
    return HttpResponse("search items")

def productview(request,myid):
    products = product.objects.filter(id = myid)
    # print(product)
    return render(request,'shop/quickview.html',{'product':products[0]})
    # ,{'product':product[0]}

def cheak(request):

    if (request.method == 'POST'):
        item_jsons = request.POST.get('itemjson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        addresh = request.POST.get('Address','') +" "+ request.POST.get('Adderss2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code  = request.POST.get('Zip_code','')
        phone = request.POST.get('Phone', '')
        
        Orders = order(item_json = item_jsons,name = name , email = email ,addresh = addresh,city = city,state = state,zip_code = zip_code,phone = phone )
        Orders.save()
        update = orderupdate(order_id = Orders.order_id ,update_desc = "The order has been placed." )
        update.save()
        id = Orders.order_id
        print (id)
        thank = True
        print (thank)
        return render(request,'shop/cheakout.html',{'thank':thank,'id':id})
    return render(request,'shop/cheakout.html')

