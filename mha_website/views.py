from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib import messages

# Create your views here.
class homeView(TemplateView):
    template_name = "home.html"

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