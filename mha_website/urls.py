from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView.as_view(), name='home'),
]