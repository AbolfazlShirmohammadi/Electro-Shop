from django.urls import path
from . import views

from django.urls import path
from . import views


urlpatterns = [

    path( '', views.cart_view, name='cart'),


    path('add/<int:id>/', views.add_to_cart,name='add_to_cart'),


    path('remove/<int:id>/',views.remove_from_cart,name='remove_from_cart'),


    path('increase/<int:id>/',views.increase_quantity,name='increase_quantity'),


    path( 'decrease/<int:id>/',views.decrease_quantity,name='decrease_quantity'),

]