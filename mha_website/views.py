from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib import messages
from .forms import *
from django.shortcuts import reverse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
class homeView(TemplateView):
    template_name = "home.html"

# Signup/Login page
class registerView(View):
    form_class = UserCreationForm
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
    
class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(auth_views.LogoutView):
    next_page = '/'

# Contact page
class SuccessView(TemplateView):
    template_name = 'success.html'

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')

        full_message = f"""
            Recieved message below from {email}, {subject}
            --------------------
            {message}
            """
            
        send_mail(
            subject='Recieved contact form submission',
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
            )
        return super(ContactView, self).form_valid(form)