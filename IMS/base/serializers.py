from rest_framework.serializers import ModelSerializer
from .models import Product, ProductType, Purchase, Supplier, Department

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'

class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'        

class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'   

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'          