from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('main',views.wellcome,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout/', LogoutView.as_view(next_page='/main'), name='logout'),
    

]

