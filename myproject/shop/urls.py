from django.urls import path
from .views import ProductListView, ProductDetailView, CartView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/cart/', CartView.as_view(), name='cart'),
    path('api/cart/<int:product_id>/', CartView.as_view(), name='cart-delete'),
]