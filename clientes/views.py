from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def list_person(request):
    persons = Person.objects.all()
    return render(request, 'persons.html', {'persons' : persons})

@login_required
def add_person(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_person')
    
    return render(request, 'new_person.html', {'form': form})

@login_required
def update_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('list_person')
    
    return render(request, 'new_person.html', {'form': form})

@login_required
def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        person.delete()
        return redirect('list_person')
    
    return render(request, 'delete_confirm.html', {'person':person})
