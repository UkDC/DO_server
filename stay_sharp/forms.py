from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import All_knifes, Grinding_data, Honing_data
from .utilities import send_email_for_varify




class All_knifesForm_step1(forms.ModelForm):
    class Meta:
        model = All_knifes
        exclude = ['carbon', 'CrMoV', 'angle', 'honing_add', 'category']


class All_knifesForm_step2(forms.ModelForm):
    class Meta:
        model = All_knifes
        exclude = ['brend', 'series', 'steel', 'angle', 'honing_add', 'category']


class Grinding_dataForm(forms.ModelForm):
    class Meta:
        model = Grinding_data
        exclude = ['USH']


class Honing_dataForm(forms.ModelForm):
    class Meta:
        model = Honing_data
        exclude = ['FVB_H']


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def save(self, commit=True, ):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def save(self, commit=True, ):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user
