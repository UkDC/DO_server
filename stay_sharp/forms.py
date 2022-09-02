from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import All_knifes, Grinding_data, Honing_data
from django.core.validators import MinValueValidator, MaxValueValidator

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


# class LoginForm(forms.Form):
#     email = forms.CharField()
#     password = forms.CharField()

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


