from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('shop/', ProductListView.as_view(), name='product-list'),
    path('shop/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]