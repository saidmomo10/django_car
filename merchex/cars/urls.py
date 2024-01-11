from django.urls import path
from . import views

urlpatterns = [
    path('/cars', views.list_car, name='cars'),
    path('cars/<str:pk>', views.show, name='car_detail'),
    path('add_car/', views.addcar, name='add_car'),
    path('update_car/<str:pk>', views.updatecar, name='update_car'),
    path('delete_car/<str:pk>', views.deletecar, name='delete_car'),
]
 