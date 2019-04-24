from django.shortcuts import render, redirect
from .forms import VendaForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def venda(request):
    form = VendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_person')
    
    return render(request, 'venda.html', {'form':form})