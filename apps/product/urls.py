from django.urls import path
from .views import (
    ProductCreateAPIView,
    ProductAPIView
)

app_name = 'product'

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='create'),
    path('<slug:slug>/detail/', ProductAPIView.as_view(), name='detail'),
    path('<slug:slug>/update/', ProductAPIView.as_view(), name='update'),
    path('<slug:slug>/delete/', ProductAPIView.as_view(), name='delete'),
]