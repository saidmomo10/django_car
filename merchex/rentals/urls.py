from django.urls import path
from . import views

urlpatterns = [
    path('add_rental/', views.addrental, name='add_rental'),
    path('update_rental/<str:pk>', views.updaterental, name='update_rental'),
    path('delete_rental/<str:pk>', views.deleterental, name='delete_rental'),
    # path('about-us/', views.about),
]
 