from django.shortcuts import render
from .models import footwear
from .form import FootwearForm
# Create your views here.

def footwear_list(request):
    prod= footwear.objects.all()
    form= FootwearForm()
    return render(request,'footwear/footwear.html',{"prod":prod})