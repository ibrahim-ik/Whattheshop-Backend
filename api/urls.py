from django.urls import path
from .views import RegisterAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
]
