
from pyexpat.errors import messages
from django.shortcuts import render

# Create your views here.
from contextlib import ExitStack
import datetime
import io, csv
from concurrent.futures.thread import _worker
from urllib import response
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render,redirect

import base64
from django.core.files.base import ContentFile

from .models import  Item
import psycopg2 
from django.contrib.auth.models import User
import base64
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

conn=psycopg2.connect(host='localhost',dbname='image',user='postgres',password='123456789',port='5432')
      



def addProduct(request):
    context = {}
    print("djkkknjkdnjncdsjncjdncskj")
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == "POST":
        prod = Item()
        
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')
        if len(request.FILES) != 0:
            
            prod.image = request.FILES['image']
            image_content = prod.image.read()
            base64_encoded = base64.b64encode(image_content).decode('utf-8')
            prod.image_base64 = base64_encoded
            image_content = base64.b64decode(base64_encoded)
            # msfilee=io.StringIO(prod.image)
            print("dskfsdfsdkfskdkfdskfksdkfdkfdskfsdkk")
            print(base64_encoded)
        
        cur.execute("INSERT INTO image_item (name, price, description, image) VALUES (%s,%s,%s,%s);",(prod.name,prod.description,prod.price,base64_encoded))
        conn.commit()
        
        return render(request, 'mansour.html' ,context)
    return render(request, 'index.html')



def addProductnormal(request):
    context = {}
  
    if request.method == "POST":
        prod = Item()
        
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')
        if len(request.FILES) != 0:
            
            prod.image = request.FILES['image']
            image_content = prod.image.read()
            base64_encoded = base64.b64encode(image_content).decode('utf-8')
            prod.image_base64 = base64_encoded
            image_content = base64.b64decode(base64_encoded)
            # msfilee=io.StringIO(prod.image)
            print("dskfsdfsdkfskdkfdskfksdkfdkfdskfsdkk")
            print(base64_encoded)
        
        c=Item.objects.create(name=prod.name,price=prod.description,description=prod.price,image=base64_encoded)
        c.save()
       
        
        return render(request, 'getnormal.html' ,context)
    return render(request, 'normal.html')







def getProductnormal(request):
    context = {}
    c=Item.objects.all()
               
    context['data']=c

    return render(request, 'getnormal.html' ,context)
   



def getProductpsycopy(request):
    context = {}
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select * from image_item;")
    
    publisher_records = cur.fetchall()
    print(publisher_records)
    
    context["data"]=publisher_records

    return render(request, 'getpsycopy.html',context)














#   image_content = base64.b64decode(base64_encoded)
    

#             decoded_image = base64.b64encode(image_content).decode('utf-8')
    
  
#             print(decoded_image)
#             context = {'decoded_image': decoded_image}