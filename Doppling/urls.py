
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # this is for the home / root rout. now it will be managed by chat app.
    path('api/',include('chat.urls')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
