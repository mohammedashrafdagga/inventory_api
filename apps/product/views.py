from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser

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
