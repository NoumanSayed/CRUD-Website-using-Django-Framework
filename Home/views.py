from django.shortcuts import render
from Footwear.models import footwear
from Clothing.models import clothing
from Accessories.models import accessories


def home(request):
    return render(request, 'Home/home.html')

def footwear_list(request):
    prod= footwear.objects.all()
    return render(request, 'footwear/footwear.html',{"prod":prod})

def clothing_list(request):
    prod= clothing.objects.all()
    return render(request,'clothing/clothing.html',{"prod":prod})

def accessories_list(request):
    prod= accessories.objects.all()
    return render(request,'Home/accessories.html',{"prod":prod})

def About_list(request):
    return render(request,'Home/About.html')

def Contact_list(request):
    return render(request,'Home/contact.html')

def Cart_list(request):
    return render(request,'Home/cart.html')