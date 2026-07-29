from django.urls import path
from . import views

urlpatterns = [
    path('information',views.info,name='information'),
]