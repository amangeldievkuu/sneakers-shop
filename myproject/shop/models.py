from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="products/")

    def __str__(self) -> str:
        return f"name: {self.name}, brand: {self.brand}, price: {self.price}"


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self) -> str:
        return f"name: {self.product.name}, quantity: {self.quantity}"