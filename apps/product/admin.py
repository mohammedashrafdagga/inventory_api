from django.contrib import admin
from .models import Product

# register Product
@admin.register(Product)
class ProductAdminI(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active','create_at')
    list_filter = ('is_active',)
    exclude = ('created_by',)
    
    def get_queryset(self, request):
        return self.model.objects.all()
        
    
    def save_model(self, request, obj, form, change):
        # for new instance -> save user 
        if not change:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)