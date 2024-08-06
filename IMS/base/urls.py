from django.urls import path
from .views import ProductApiView, ProductTypeApiView, PurchaseApiView, SupplierApiView, DepartmentApiView

urlpatterns = [
    path('product/', ProductApiView.as_view({'get':'list', 'post':'create'})),
    path('product/<int:pk>/', ProductApiView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('producttype/', ProductTypeApiView.as_view({'get':'list', 'post':'create'})),
    path('producttype/<int:pk>/', ProductTypeApiView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('purchase/', PurchaseApiView.as_view({'get':'list', 'post':'create'})),
    path('purchase/<int:pk>/', PurchaseApiView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('supplier/', SupplierApiView.as_view({'get':'list', 'post':'create'})),
    path('supplier/<int:pk>/', SupplierApiView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('department/', DepartmentApiView.as_view({'get':'list', 'post':'create'})),
    path('department/<int:pk>/', DepartmentApiView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}))
]