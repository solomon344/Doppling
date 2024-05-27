from rest_framework.serializers import ModelSerializer
from .models import (Message,Group,User,Profile)


# creating serializers for each model

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','username']

class ProfileSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    by = UserSerializer()
    class Meta:
        model = Message
        fields = '__all__'

class GroupSerializer(ModelSerializer):
    members = UserSerializer(many=True)
    messages = MessageSerializer(many=True)
    class Meta:
        model = Group
        fields = '__all__'