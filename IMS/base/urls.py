from django.urls import path
from .views import group_list, register, login, ProductApiView, ProductTypeApiView, ProductTypeApiDetailView, PurchaseApiView, SupplierApiView, DepartmentApiView

urlpatterns = [
    path('groups/', group_list),
    path('login/', login),
    path('register/', register),
    path('product/', ProductApiView.as_view({'get':'list', 'post':'create'})),
    path('product/<int:pk>/', ProductApiView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('product-type/', ProductTypeApiView.as_view()),
    path('product-type/<int:pk>/', ProductTypeApiDetailView.as_view()),
    path('purchase/', PurchaseApiView.as_view({'get':'list', 'post':'create'})),
    path('purchase/<int:pk>/', PurchaseApiView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('supplier/', SupplierApiView.as_view({'get':'list', 'post':'create'})),
    path('supplier/<int:pk>/', SupplierApiView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('department/', DepartmentApiView.as_view({'get':'list', 'post':'create'})),
    path('department/<int:pk>/', DepartmentApiView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}))
]