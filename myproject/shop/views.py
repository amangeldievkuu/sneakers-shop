from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer

# Create your views here.

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user)
        else:
            return Response({"detail": "Authentication required."}, status=401)
        
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def delete(self, request, product_id):
        Cart.objects.filter(user=request.user, product_id=product_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)