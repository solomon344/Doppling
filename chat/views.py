from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUp, LogIn
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from rest_framework.views import APIView
from .models import (Profile,User,Message,Group,OTP)
from .serializers import (UserSerializer,ProfileSerializer,MessageSerializer,GroupSerializer)
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from random import choices
from string import digits,punctuation,ascii_letters
from .send_email import send_login_email_OTP
from .Custom_Verifiers import Otp_Verify
import json

import os

from django.shortcuts import render


# Create your views here.

def simple_home(request):
    return render(request,'otp.html')


@csrf_exempt
def Sign_Up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'You\'ve successful sign up', 'user': username}, status=201)
            else:
                return JsonResponse({'error': 'Authentication failed'}, status=400)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@ensure_csrf_cookie
def Log_In(request):
    if request.method == 'POST':
        form = LogIn(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Login successful', 'user': username}, status=200)
            else:
                return JsonResponse({'error': 'Invalid username or password'}, status=400)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def Log_Out(request):
    if request.method == 'POST':
        
        logout(request)
        return JsonResponse({'message': 'Logout successful'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

class APi_Login(APIView):
    permission_classes = [AllowAny,]
    def post(self,request,*args,**kwargs):
        email = request.data['email']
        password = request.data['password']
        user_ref = User.objects.get(email=email)

        user = authenticate(request,username=user_ref.username,password=password)
        
        if user is not None:
            otp_gen = ''.join(choices([i for i in digits],k=4))

            OTP.objects.create(otp=otp_gen,email=email)
            OTP.save()
            try:
                send_login_email_OTP(to=[email,],otp=otp_gen,subject='OTP')
            except:
                print(f'There was a problem sending otp em to {email}')

            otp = {
                'otp':otp_gen
            }
            

              
            
            return Response(otp,status.HTTP_200_OK)
        return Response({'message':'No user found with this email'},status.HTTP_404_NOT_FOUND)
    

class APi_Otp_Verify(APIView):
    
    def post(self,request,*args,**kwargs):
        otp = request.data['otp']

        if otp:
            otp_verify = Otp_Verify(otp)
            if otp_verify.is_valid():
                gen_token = RefreshToken.for_user(otp_verify.get_user()),
                token = {
                    'access':str(gen_token.access_token),
                    'refresh':str(gen_token)
                }

                return Response(token,status=status.HTTP_200_OK)
            return Response({'message':'Invalid Token'},status.HTTP_404_NOT_FOUND)
    

    


class User_ViewSet(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self,request,*args,**kwargs):
        pk = request.query_params.get('id')
        if pk:
            query = User.objects.get(pk=pk)
            if query:
                serializer = UserSerializer(query)
                return Response(serializer.data,200)
                
            else:
                 return Response({'message':'user not found'},403)
        else:
            query = User.objects.all()
            serializer = UserSerializer(query,many=True)
            return Response(serializer.data,200)
        
    def post(self,request,*args,**kwargs):
        data = request.data
        pk = kwargs['id']
        if pk:
            query = User.objects.get(pk=pk)
            serializer = UserSerializer(query,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'user updated successfully'},200)
            return Response({'message':'invalid data provided'},status.HTTP_406_NOT_ACCEPTABLE)
        else:
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'account created successfully'},200)
            return Response({'message':'invalid data provided'},status.HTTP_406_NOT_ACCEPTABLE)



        