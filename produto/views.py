from django.shortcuts import render, redirect
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def cad_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_person')
    
    return render(request, 'produto.html', {'form': form})