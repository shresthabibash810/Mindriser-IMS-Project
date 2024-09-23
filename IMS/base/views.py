from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, ProductType, Purchase, Supplier, Department
from rest_framework.generics import GenericAPIView
from .serializers import GroupSerializer, UserSerializer, ProductSerializer, ProductTypeSerializer, PurchaseSerializer, SupplierSerializer, DepartmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAuthenticated
from .permissions import CustomPermisiion
from django.contrib.auth.models import Group

@api_view(['GET'])
@permission_classes([AllowAny])
def group_list(request):
    group_objs = Group.objects.all()
    serializer = GroupSerializer(group_objs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    password = request.data.get('password')
    hash_password = make_password(password)
    request.data['password'] = hash_password
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Registration Successful')
    else:
        return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)

    if user == None:
        return Response('Invalid Credentials')
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)

# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['department', 'type']
    search_fields = ['name']

    # @property
    # def __str__(self) -> str:
    #     return super().__str__()

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

class ProductTypeApiView(GenericAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated, CustomPermisiion]
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Created!')
        else:
            return Response(serializer.errors)

class ProductTypeApiDetailView(GenericAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get(self, request, pk):   
        queryset = self.get_object()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)        
    
    def put(self, request, pk):
        queryset = self.get_object()
        serializer = self.serializer_class(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Updated!')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        queryset = self.get_object()
        queryset.delete()
        return Response('Data Deleted')

class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer  

class SupplierApiView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer 

class DepartmentApiView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer