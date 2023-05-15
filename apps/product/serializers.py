from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        exclude = ('image',)
        read_only_fields = ('created_by',)  # To prevent updating 'created_by' field directly

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user
        return super().create(validated_data)
