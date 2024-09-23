from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=300, default='username', unique=True)
    password = models.CharField(max_length=300)
    contact = models.BigIntegerField(null=True)
    location = models.CharField(max_length=300)
    image = models.ImageField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class ProductType(models.Model):
    name = models.CharField(max_length=300)

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    size = models.CharField(max_length=300)
    price = models.IntegerField()
    quantity = models.IntegerField()
    department = models.ManyToManyField('Department', null=True)
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)    

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.ForeignKey('Supplier', models.SET_NULL, null=True)

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    contact = models.BigIntegerField()
    location = models.CharField(max_length=300)
    email = models.EmailField()

class Department(models.Model):
    name = models.CharField(max_length=300)
    floor = models.IntegerField()
    description = models.TextField()


