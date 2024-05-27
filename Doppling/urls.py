
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)


urlpatterns = [
    path('admin/', admin.site.urls),
    # this is for the home / root rout. now it will be managed by chat app.
    path('',include('chat.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
