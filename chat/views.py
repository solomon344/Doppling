from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUp, LogIn
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


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

@csrf_exempt
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
