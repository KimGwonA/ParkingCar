from django import forms
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.modelfields import PhoneNumberField

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"placeholder": "사용자명 (3자리 이상)"},
        ),
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호 (4자리 이상)"},
        ),
    )

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    carNumber = forms.CharField(min_length=3)
    address = forms.CharField(min_length=5)
    phoneNumber = forms.CharField(min_length=8)

