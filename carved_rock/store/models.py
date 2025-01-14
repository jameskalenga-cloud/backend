from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="")
    sku = models.CharField(verbose_name="stock keeping unit", max_length=20, unique=True, default="")


class ProductImage(models.Model):
    image = models.ImageField()
    Product = models.ForeignKey('Product', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product')