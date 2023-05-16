from rest_framework import serializers
from .models import Product
from django.utils.text import slugify


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_empty_file=True, required=False)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_by',)  # To prevent updating 'created_by' field directly

    def create(self, validated_data):
        # put create user into product
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user
            
        # change rename product into application
        # we need pop image from validated data
        validated_data.pop('image')
        product = Product.objects.create(**validated_data)
        image = request.data.get('image')
        if image:
            image.name = f"{slugify(product.name)}_{product.id}.{image.name.split('.')[-1]}"
            product.image = image
            product.save()
        return product


