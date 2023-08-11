from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.

# Create your views here.
#django support 2 type of views !! function based views and class based views

def home(request):
    return HttpResponse("Royal Technosoft")

def aboutus(request):
    return render(request,"expenseapp/aboutUs.html")

def contactus(request):
    return render(request,"expenseapp/contactUs.html")


def getProduct(request):
    # products=Product.objects.all()  #select * from product
    # products=Product.objects.all().values_list()
    products=Product.objects.all().values()
    # print(products)
    context={"products":products,"age":2}
    return render(request,"product/product_details.html",context)


def getBook(request):
    book=Books.objects.all().values()
    context={"book":book}
    print(book)
    return render(request,"book/book_details.html",context)