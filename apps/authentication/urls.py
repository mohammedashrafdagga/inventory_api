from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import LoginAPIView, LogoutAPIView



app_name = 'authentication'

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name= 'login'),
    path('logout/', LogoutAPIView.as_view(), name= 'logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]