
from django.urls import path
from Footwear import views

app_name ='Footwear'

urlpatterns = [
    path('footwear/', views.footwear_list, name='footwear')
]

