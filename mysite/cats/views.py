from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat, Breed


class CatList(LoginRequiredMixin, View):
    def get(self, request):
        breed_counter = Breed.objects.all().count()
        cats_list = Cat.objects.all()
        ctx = {'breed_counter': breed_counter, 'cats_list': cats_list}

        return render(request, 'cats/cats_list.html', ctx)


class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        ctx = {'breed_list': Breed.objects.all()}
        return render(request, 'cats/breed_list.html', ctx)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
