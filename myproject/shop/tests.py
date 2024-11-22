from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product, Cart
# Create your tests here.

class APITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin')

        self.product = Product.objects.create(
            name="Test Sneaker",
            brand="Test Brand",
            category="Shoes",
            price=99.99,
            stock=10
        )

        self.client = APIClient()

        self.client.login(username='admin', password='admin')

    def test_get_products(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_product_detail(self):
        response = self.client.get(reverse('product-detail', args=[self.product.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Adidas zoom")

    def test_add_to_cart(self):
        data = {"product": self.product.id, "quantity": 1}
        response = self.client.post(reverse('cart'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cart.objects.count(), 1)

    def test_get_cart(self):
        Cart.objects.create(user=self.user, product=self.product, quantity=2)
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_delete_from_cart(self):
        cart_item = Cart.objects.create(user=self.user, product=self.product, quantity=2)
        response = self.client.delete(reverse('cart-delete', args=[cart_item.product.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cart.objects.count(), 0)
