from django.urls import path
from . import views

urlpatterns = [
    path('add_category/', views.addcategory, name='add_category'),
    path('/category_list', views.categorylist, name='category_list'),

    path('update_category/<str:pk>', views.updatecategory, name='update_category'),
    path('delete_category/<str:pk>', views.deletecategory, name='delete_category'),
    # path('about-us/', views.about),
]
 