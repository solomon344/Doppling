from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name='home'),
    
    # your extra routes here.
    path('login',views.Log_In,name="login"),
    path('logout',views.Log_Out,name="logout"),
    path('signup',views.Sign_Up,name="signup")
]