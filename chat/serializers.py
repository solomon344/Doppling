from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import (Message,Group,User,Profile)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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

# class Token_Custom_Serializer(TokenObtainPairSerializer):
#     username_field = 'email'
#     @classmethod
#     def get_token(cls, user: user) -> Token:
#         return super().get_token(user)