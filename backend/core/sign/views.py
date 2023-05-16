from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group
from .models import BaseRegisterForm
from django.urls import reverse_lazy


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = reverse_lazy('home')