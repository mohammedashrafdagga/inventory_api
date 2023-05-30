from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductAPIView,
    CategoryCreateAPIView,
    TagCreateAPIView
)

app_name = 'product'

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='list'),
    path('create/', ProductListCreateAPIView.as_view(), name='create'),
    path('<slug:slug>/detail/', ProductAPIView.as_view(), name='detail'),
    path('<slug:slug>/update/', ProductAPIView.as_view(), name='update'),
    path('<slug:slug>/delete/', ProductAPIView.as_view(), name='delete'),
    path('<slug:slug>/assign-image/', ProductAPIView.as_view(), name='assign-image'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('tag/create/', TagCreateAPIView.as_view(), name='tag-create'),
    path('<slug:slug>/assign-tags/', ProductAPIView.as_view(), name='assign-tags'),
    path('<slug:slug>/assign-category/', ProductAPIView.as_view(), name='assign-category'),
]