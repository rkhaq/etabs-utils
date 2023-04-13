# accounts/urls.py
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import GoogleLogin

from .views import CustomTokenObtainPairView, UserRegistrationView

urlpatterns = [
    # path('api/register/', UserRegistrationView.as_view(), name='register'),
    # path('api/auth/token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    # path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    path('api/google/', GoogleLogin.as_view(), name='google_login'),
]
