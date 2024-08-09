from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
import requests

# Template view pages
class homeView(TemplateView):
    template_name = "home.html"

class privacyView(TemplateView):
    template_name = "privacy_policy.html"

class faqView(TemplateView):
    template_name = "faq.html"
class aboutView(TemplateView):
    template_name = "about.html"

# Signup/Login page
class registerView(View):
    form_class = CustomSignUpForm
    template_name = "registration/signup.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        return render(request, self.template_name, {'form': form})
    
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "registration/login.html"
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        return render(request, self.template_name, {'form': form})

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect("home")

# Contact page
class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
            'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            print(f"Received reCAPTCHA response: {recaptcha_response}")  # Debugging line
            data = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            print(f"reCAPTCHA verification result: {result}")  # Debugging line

            if result['success'] and result['score'] >= 0.5:
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']

                send_mail(
                    subject,
                    message,
                    email,
                    recipient_list= [settings.NOTIFY_EMAIL]
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')

            else:
                messages.error(request, 'Our form seems to think you are a robot, if you are not please try again!')

        context = {
            'form': form,
            'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY
        }    
        return render(request, self.template_name, context)