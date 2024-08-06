from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, ProductType, Purchase, Supplier, Department
from .serializers import ProductSerializer, ProductTypeSerializer, PurchaseSerializer, SupplierSerializer, DepartmentSerializer

# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer  

class SupplierApiView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer 

class DepartmentApiView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer