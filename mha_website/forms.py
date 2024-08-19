from django import forms
from django_recaptcha.fields import ReCaptchaV3
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .choices import *

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
        help_text="150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"})
    )
    password1 = forms.CharField(
        help_text="Your password can't be too similar to your username. Your password must contain at least 8 characters. Your password can't be a commonly used password. Your password can't be entirely numeric.",
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"})
    )
    password2 = forms.CharField(
        help_text="Enter the same password as before, for verification.",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password", "class": "form-control"})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomLoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"})
    )

class CustomCardSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="Card Name",
        widget=forms.TextInput(attrs={"placeholder": "Card Name", "class": "form-control"})
    )
    
    rarity = forms.MultipleChoiceField(
        required=False,
        label="Rarity",
        choices=rarityChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )
    
    set = forms.ChoiceField(
        required=False,
        label="Set",
        choices=setChoices,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    cardType = forms.MultipleChoiceField(
        required=False,
        label="Card Type",
        choices=cardTypeChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )
    
    symbol = forms.MultipleChoiceField(
        required=False,
        label="Symbol",
        choices=symbolChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )
    
    keywords = forms.MultipleChoiceField(
        required=False,
        label="Keywords",
        choices=keywordChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    control = forms.MultipleChoiceField(
        required=False,
        label="Control",
        choices=controlChoice,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    difficulty = forms.IntegerField(
        required=False,
        label="Difficulty",
        widget=forms.NumberInput(attrs={"placeholder": "Difficulty", "class": "form-control"})
    )

    blockZone = forms.MultipleChoiceField(
        required=False,
        label="Block Zone",
        choices=zoneChoice,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    blockModifier = forms.IntegerField(
        required=False,
        label="Block Modifier",
        widget=forms.NumberInput(attrs={"placeholder": "Block Modifier", "class": "form-control"})
    )

    attackZone = forms.MultipleChoiceField(
        required=False,
        label="Attack Zone",
        choices=zoneChoice,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    speed = forms.IntegerField(
        required=False,
        label="Speed",
        widget=forms.NumberInput(attrs={"placeholder": "Speed", "class": "form-control"})
    )

    damage = forms.IntegerField(
        required=False,
        label="Damage",
        widget=forms.NumberInput(attrs={"placeholder": "Damage", "class": "form-control"})
    )

    cardText = forms.CharField(
        required=False,
        label="Card Text",
        widget=forms.TextInput(attrs={"placeholder": "Card Text", "class": "form-control"})
    )

class AdminAddCardForm(forms.Form):
    name = forms.CharField(
        required=True,
        label="Card Name",
        widget=forms.TextInput(attrs={"placeholder": "Card Name", "class": "form-control"})
    )

    image = forms.URLField(
        required=True,
        label="Image URL",
        widget=forms.URLInput(attrs={"placeholder": "Insert URL here", "class": "form-control"})
    )
    
    rarity = forms.MultipleChoiceField(
        required=True,
        label="Rarity",
        choices=rarityChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )
    
    set = forms.ChoiceField(
        required=True,
        label="Set",
        choices=setChoices,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    cardType = forms.MultipleChoiceField(
        required=True,
        label="Card Type",
        choices=cardTypeChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )
    
    symbol = forms.MultipleChoiceField(
        required=True,
        label="Symbol",
        choices=symbolChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )
    
    keywords = forms.MultipleChoiceField(
        required=True,
        label="Keywords",
        choices=keywordChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    control = forms.MultipleChoiceField(
        required=True,
        label="Control",
        choices=controlChoice,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    difficulty = forms.IntegerField(
        required=True,
        label="Difficulty",
        widget=forms.NumberInput(attrs={"placeholder": "Difficulty", "class": "form-control"})
    )

    blockZone = forms.MultipleChoiceField(
        required=True,
        label="Block Zone",
        choices=zoneChoice,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    blockModifier = forms.IntegerField(
        required=True,
        label="Block Modifier",
        widget=forms.NumberInput(attrs={"placeholder": "Block Modifier", "class": "form-control"})
    )

    attackZone = forms.MultipleChoiceField(
        required=True,
        label="Attack Zone",
        choices=zoneChoice,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    speed = forms.IntegerField(
        required=True,
        label="Speed",
        widget=forms.NumberInput(attrs={"placeholder": "Speed", "class": "form-control"})
    )

    damage = forms.IntegerField(
        required=True,
        label="Damage",
        widget=forms.NumberInput(attrs={"placeholder": "Damage", "class": "form-control"})
    )

    cardText = forms.CharField(
        required=True,
        label="Card Text",
        widget=forms.TextInput(attrs={"placeholder": "Card Text", "class": "form-control"})
    )