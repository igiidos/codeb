from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # 이메일 필드 추가

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")