from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # user_type = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super(UserRegisterForm, self).save(commit=True)
    #     user.user_type = self.cleaned_data["user_type"]
    #     if commit:
    #         user.save()
    #     return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','user_type']


class ProfileUserTypeUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['user_type']
