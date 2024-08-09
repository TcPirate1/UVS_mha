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
        label="Card Name",
        widget=forms.TextInput(attrs={"placeholder": "Card Name", "class": "form-control"})
    )
    rarityChoices = [
        ("Common", "Common"),
        ("Uncommon", "Uncommon"),
        ("Rare", "Rare"),
        ("SE", "SE"),
        ("Super Rare", "Super Rare"),
        ("Ultra Rare", "Ultra Rare"),
        ]
    
    rarity = forms.MultipleChoiceField(
        label="Rarity",
        choices=rarityChoices,
        widget=forms.MultipleChoiceField(attrs={"class": "form-check-input"})
    )

    setChoices = [
        ("Base Set", "Base Set"),
        ("Promo Set", "Promo Set"),
        ("Expansion Set", "Expansion Set"),
        ("Starter Set", "Starter Set"),
        ("Booster Set", "Booster Set"),
        ("Special Edition Set", "Special Edition Set"),
        ("Crimson Rampage", "Crimson Rampage"),
        ("Heroes Clash", "Heroes Clash"),
        ("League of Villans", "League of Villans"),
        ("Undaunted Raid", "Undaunted Raid"),
        ("Jet Burn", "Jet Burn"),
        ("Girl Power", "Girl Power"),
        ("DLC", "DLC"),
        ("Other", "Other"),
        ]
    
    set = forms.ChoiceField(
        label="Set",
        choices=setChoices,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    cardTypeChoices = [
        ("Character", "Character"),
        ("Action", "Action"),
        ("Asset", "Asset"),
        ("Attack", "Attack"),
        ("Foundation", "Foundation"),
        ("Backup", "Backup"),
    ]

    cardType = forms.MultipleChoiceField(
        label="Card Type",
        choices=cardTypeChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    symbolChoices = [
        ("All", "All"),
        ("Air", "Air"),
        ("Earth", "Earth"),
        ("Fire", "Fire"),
        ("Life", "Life"),
        ("Death", "Death"),
        ("Good", "Good"),
        ("Evil", "Evil"),
        ("Order", "Order"),
        ("Chaos", "Chaos"),
        ("Infinity", "Infinity"),
        ]
    
    symbol = forms.MultipleChoiceField(
        label="Symbol",
        choices=symbolChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    keywordChoices = [
        ("All", "All"),
        ("Combo", "Combo"),
        ("Enhance", "Enhance"),
        ("Guard", "Guard"),
        ("Power Up", "Power Up"),
        ("Stun", "Stun"),
        ("Throw", "Throw"),
        ("Unique", "Unique"),
        ]
    
    keywords = forms.MultipleChoiceField(
        label="Keywords",
        choices=keywordChoices,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )
    controlChoice = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ]

    control = forms.MultipleChoiceField(
        label="Control",
        choices=controlChoice,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    difficulty = forms.IntegerField(
        label="Difficulty",
        widget=forms.NumberInput(attrs={"placeholder": "Difficulty", "class": "form-control"})
    )

    blockZoneChoice = [
        ("High", "High"),
        ("Mid", "Mid"),
        ("Low", "Low"),
        # Reused for Attack Zone
    ]

    blockZone = forms.MultipleChoiceField(
        label="Block Zone",
        choices=blockZoneChoice,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    blockModifier = forms.IntegerField(
        label="Block Modifier",
        widget=forms.NumberInput(attrs={"placeholder": "Block Modifier", "class": "form-control"})
    )

    attackZone = forms.MultipleChoiceField(
        label="Attack Zone",
        choices=blockZoneChoice,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
    )

    speed = forms.IntegerField(
        label="Speed",
        widget=forms.NumberInput(attrs={"placeholder": "Speed", "class": "form-control"})
    )

    damage = forms.IntegerField(
        label="Damage",
        widget=forms.NumberInput(attrs={"placeholder": "Damage", "class": "form-control"})
    )

    cardText = forms.CharField(
        label="Card Text",
        widget=forms.TextInput(attrs={"placeholder": "Card Text", "class": "form-control"})
    )