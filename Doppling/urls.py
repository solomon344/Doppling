
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # this is for the home / root rout. now it will be managed by chat app.
    path('',include('chat.urls'))
]
