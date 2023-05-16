from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import generics
from .models import Product


class ProductMixin():
    queryset = Product.items.all()
    serializer_class = ProductSerializer
    
    
# Product Create API View
class ProductListCreateAPIView(ProductMixin, generics.ListCreateAPIView):
    pass
    
  
# Retrieve API View
class ProductAPIView(ProductMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    
