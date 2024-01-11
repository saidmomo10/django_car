from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:pk>', views.show, name='custom'),
    path('add_customer/', views.addcustomer, name='add_customer'),
    path('update_customer/<str:pk>', views.updatecustomer, name='update_customer'),
    path('delete_customer/<str:pk>', views.deletecustomer, name='delete_customer'),
    # path('about-us/', views.about),
]
 