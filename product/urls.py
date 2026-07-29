from django.urls import path
from . import views






urlpatterns = [
    path('list',views.product,name='product_list'),
    path('category/<int:id>',views.category_list,name='category_list'),
    path('product_detail/<int:id>',views.product_detail,name='product_detail'),
    path('add-product', views.add_product_view, name='add_product'),
    path('my-products/',views.my_products_view, name='my_products'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('live-search/', views.live_search_view, name='live_search'),

]