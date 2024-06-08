from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    # path('',views.home,name='home'),
    
    # your extra routes here.
    path('login',views.Log_In,name="login"),
    path('logout',views.Log_Out,name="logout"),
    path('signup',views.Sign_Up,name="signup"),
    path('user',views.User_ViewSet.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api_login',views.APi_Login.as_view()),
    path('',views.simple_home,name='home')
]