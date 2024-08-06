from django import forms
from django_recaptcha.fields import ReCaptchaV3

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Subject"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )
    captcha = ReCaptchaV3()