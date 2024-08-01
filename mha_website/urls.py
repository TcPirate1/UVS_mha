from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('signup/', registerView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('success/', SuccessView.as_view(), name='success'),
]