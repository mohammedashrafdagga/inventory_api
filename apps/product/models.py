from django.db import models
from django.contrib.auth.models import User
import uuid


class CustomProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)

class Product(models.Model):
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.SET_NULL, null=True, blank=True) 
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default=uuid.uuid4())
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    # items 
    items = CustomProductManager()
    
    
    class Meta:
        ordering = ('-create_at', )
    
    
    def __str__(self):
        return self.name
    
    
    
    
# Category and Tags Model
class Category(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='categories')
    name = models.CharField(max_length=255)
    slug = models.SlugField(    unique=True) 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    
    
    
    
class Tag(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tags')
    name = models.CharField(max_length=255)
    slug = models.SlugField( unique=True) 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    