from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField()
    country = models.CharField(max_length=100)
    dof = models.DateField()
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.user.username

class Message(models.Model):
    content = models.TextField()
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.by.username

class Group(models.Model):
    members = models.ManyToManyField(User)
    messages = models.ManyToOneRel(field=Message, field_name='id', to=Message)
    created_at =  models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by.username

