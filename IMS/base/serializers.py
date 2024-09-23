from rest_framework.serializers import ModelSerializer
from .models import User, Product, ProductType, Purchase, Supplier, Department
from django.contrib.auth.models import Group

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'groups', 'password', 'contact', 'location', 'image']
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
        model = Department
        fields = '__all__'          