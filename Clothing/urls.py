
from django.urls import path
from Clothing import views

app_name ='Clothing'

urlpatterns = [
    path('clothing/', views.clothing_list, name='clothing')
]