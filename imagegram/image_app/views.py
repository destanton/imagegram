from django.shortcuts import render
from image_app.models import Image, Comment
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class ImageListView(ListView):
    model = Image


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('image_list_view')


class ImageCreateView(CreateView):
    model = Image
    fields = ('title', 'description', 'nsfw', 'picture')
    success_url = reverse_lazy('image_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class ImageDetailView(DetailView):
    model = Image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image"] = Image.objects.filter(id=self.kwargs['pk'])
        # context["comment"] = Comment.objects.all()
        return context


class ImageUpdateView(UpdateView):
    model = Image
    fields = ('title', 'description', 'nsfw', 'picture')
    success_url = reverse_lazy('image_list_view')


class ImageDeleteView(DeleteView):
    model = Image
    fields = ('title', 'description', 'nsfw', 'picture')
    success_url = reverse_lazy('image_list_view')


class CommentCreateView(CreateView):
    model = Comment
    fields = ('comment',)
    # success_url = reverse_lazy('image_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.image = Image.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('image_detail_view', args=[int(self.kwargs['pk'])])
