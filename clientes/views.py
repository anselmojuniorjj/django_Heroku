from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# -------------Function based view----------------------------------

# @login_required
# def list_person(request):
#     persons = Person.objects.all()
#     return render(request, 'persons.html', {'persons': persons})


# @login_required
# def add_person(request):
#     form = PersonForm(request.POST or None, request.FILES or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('list_person')
#
#     return render(request, 'new_person.html', {'form': form})


# @login_required
# def update_person(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonForm(request.POST or None, request.FILES or None, instance=person)
#
#     if form.is_valid():
#         form.save()
#         return redirect('list_person')
#
#     return render(request, 'new_person.html', {'form': form})


# @login_required
# def delete_person(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#
#     if request.method == 'POST':
#         person.delete()
#         return redirect('person_list')
#
#     return render(request, 'delete_confirm.html', {'person': person})


# ------------ Refatorando para class based view -----------------------------


class PersonList(LoginRequiredMixin, ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['footer'] = ' - Person List'
        return context


class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['footer'] = ' - Person Detail'
        return context


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'adress', 'photo']
    success_url = reverse_lazy('person_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['footer'] = ' - Person Create'
        return context

class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'adress', 'photo']
    success_url = reverse_lazy('person_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['footer'] = ' - Person Update'
        return context

class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('person_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['footer'] = ' - Person Delete'
        return context