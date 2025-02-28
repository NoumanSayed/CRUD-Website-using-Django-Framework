
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('footwear/', views.footwear_list, name='footwear'),  
    path('clothing/', views.clothing_list, name='clothing'),
    path('Home/accessories/',views.accessories_list,name='accessories'),
    path('Home/About/',views.About_list,name='About'),
    path('Home/contact/',views.Contact_list,name='Contact'),
    path('Home/cart/',views.Cart_list,name='cart'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)