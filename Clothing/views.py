from django.shortcuts import render
from .models import clothing

# Create your views here.
    

def clothing_list(request):
    prod= clothing.objects.all()
    return render(request,'clothing/clothing.html',{"prod":prod})


    


