from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm, ProfileUserTypeUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from info.models import Activities, HashTable
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # p_form = ProfileUserTypeUpdateForm(request.POST)
        if form.is_valid(): #and p_form.is_valid():
            form.save()
            # p_form.save()
            # user_type = p_form.cleaned_data.get('user_type')
            username = form.cleaned_data.get('username')

            messages.success(request, f'Account created for {username}! You can now login to access the site ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated!')
        return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'u_form': u_form,
    'p_form': p_form
    }



    return render(request, 'users/profile.html', context)

class UserAPIView(APIView):

    def get(self, request):
        user1 = User.objects.all()
        serializers = UserSerializer(user1, many=True)
        return Response(serializers.data)
