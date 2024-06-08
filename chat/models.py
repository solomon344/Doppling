from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='media/user_profiles',null=True,blank=True)
    country = models.CharField(max_length=100)
    dof = models.DateField()
    age = models.IntegerField()
    phone = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self) -> str:
        return self.user.username

class Message(models.Model):
    content = models.TextField()
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.by.username

class Group(models.Model):
    picture = models.ImageField(upload_to='media/group_profiles',null=True,blank=True)
    members = models.ManyToManyField(User)
    messages = models.ManyToOneRel(field=Message, field_name='id', to=Message)
    created_at =  models.DateTimeField(auto_now_add=True)
    created_by = models.ManyToOneRel(field=User,field_name='id',to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by.username

class OTP(models.Model):
    otp = models.CharField(max_length=6)
    email = models.EmailField()

    def __str__(self):
        return self.otp

