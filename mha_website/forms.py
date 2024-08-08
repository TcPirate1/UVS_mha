from django import forms
from django_recaptcha.fields import ReCaptchaV3
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail", "class": "form-control"})
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Subject", "class": "form-control"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message", "class": "form-control"})
    )
    captcha = ReCaptchaV3()

class CustomSignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        help_text="150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"})
    )
    password1 = forms.CharField(
        label="Password",
        help_text="Your password can't be too similar to your other personal information. Your password must contain at least 8 characters. Your password can't be a commonly used password. Your password can't be entirely numeric.",
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm password",
        help_text="Enter the same password as before, for verification.",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password", "class": "form-control"})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']