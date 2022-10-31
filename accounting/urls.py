from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from accounting import views


urlpatterns = [
    path('api/token/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/token/logout/', views.LogoutView.as_view(), name='auth_logout'),
]