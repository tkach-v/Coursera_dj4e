from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Auto, Make


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        make_count = Make.objects.all().count()
        auto_lst = Auto.objects.all()

        ctx = {"make_count": make_count, "auto_list": auto_lst}
        return render(request, 'autos/auto_list.html', ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        makes = Make.objects.all()
        ctx = {'make_list': makes}
        return render(request, 'autos/make_list.html', ctx)


class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
