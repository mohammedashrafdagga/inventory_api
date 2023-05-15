from django.urls import path
from .views import (
    ProductCreateAPIView,
    ProductDetailView,
    ProductUpdateView,
    ProductDestroyView
)

app_name = 'product'

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='create'),
    path('<slug:slug>/detail/', ProductDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', ProductUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', ProductDestroyView.as_view(), name='delete'),
]