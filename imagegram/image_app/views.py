from django.shortcuts import render
from image_app.models import Image
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class ImageListView(ListView):
    model = Image


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("image_list_view")
