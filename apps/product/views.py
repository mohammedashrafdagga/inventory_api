from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from .models import Product

class ProductCreateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            image_file = request.FILES.get('image')
            product  = serializer.save()
            product.image = image_file
            product.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# detail View
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.items.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
# update product api view
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.items.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
    
# delete product api view
class ProductDestroyView(generics.DestroyAPIView):
    queryset = Product.items.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'