from django.contrib import admin
from .models import (Message,Group)

# Register your models here.
admin.site.register(Group)
admin.site.register(Message)
