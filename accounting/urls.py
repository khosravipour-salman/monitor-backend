from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from accounting import views


urlpatterns = [
    path('token/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('token/logout/', views.LogoutView.as_view(), name='auth_logout'),

    path('register/intern/', views.RegisterIntern.as_view()),
]