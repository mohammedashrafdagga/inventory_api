from rest_framework import serializers
from .models import Product
from django.utils.text import slugify
import uuid
import os
from django.conf import settings



def generate_uuid():
    return uuid.uuid4()

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_empty_file=True, required=False)
    slug = serializers.SlugField(required=False)
    is_active = serializers.BooleanField(default=True)
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
        
        image = request.data.get('image') or None
        if image:
            validated_data.pop('image')
            product = Product.objects.create(slug= generate_uuid(), **validated_data)
            image.name = f"{slugify(product.name)}_{product.id}.{image.name.split('.')[-1]}"
            product.image = image
            product.save()
        return product

    
    def update(self, instance, validated_data):

        # Perform any additional operations if needed
        image = self.context['request'].data.get('image')
        if image:
            validated_data.pop('image')
            instance = super().update(instance, validated_data)
            old_image = instance.image
            if old_image:
                path = os.path.join(settings.MEDIA_ROOT, str(old_image))
                if os.path.exists(path):
                    os.remove(path)
            image.name = f"{slugify(instance.name)}_{instance.id}.{image.name.split('.')[-1]}"
            instance.image = image
            instance.save()
            return instance
        # Save the instance
        super().update(instance, validated_data)

        return instance