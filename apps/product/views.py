
from .serializers import ProductSerializer
from rest_framework import generics
from .models import Product


# Product Create API View
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.items.all()
    serializer_class = ProductSerializer
    
  
# Retrieve API View
class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.items.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
    
    
    