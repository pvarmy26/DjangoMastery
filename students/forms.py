from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)
from django.contrib.auth.models import User
from .models import UploadedDocument


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    course = forms.CharField(max_length=100)
    marks = forms.IntegerField()


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    pass

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ["title", "file"]