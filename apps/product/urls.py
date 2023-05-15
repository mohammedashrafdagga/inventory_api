from django.urls import path
from .views import ProductCreateAPIView

app_name = 'product'

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='create'),
]