from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, TagSerializer
from rest_framework import generics
from .models import Product, Category, Tag


class ProductMixin():
    queryset = Product.items.all()
    serializer_class = ProductSerializer
    
    
# Product Create API View
class ProductListCreateAPIView(ProductMixin, generics.ListCreateAPIView):
    pass
    
  
# Retrieve API View
class ProductAPIView(ProductMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    


# Category Create Api View Serializer
class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    

    
class TagCreateAPIView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    