from django.urls import path, include
from .views import *

urlpatterns = [
    path('', stores, name='stores'),
    path('store/<str:store_id>', store, name='store'),
    path('product/<str:product_id>', product, name='product'),
    path('product/category/<str:category_id>', category, name='category'),
]
