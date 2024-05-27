from django.contrib import admin
from .models import (Message,Group,Profile)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Message)
