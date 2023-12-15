from django.urls import path
from .views import ProductsAPIView, ProductsDetailAPIView

urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('products/<int:pk>/', ProductsDetailAPIView.as_view(), name='products-detail'),

]
