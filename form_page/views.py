
from django.shortcuts import render, redirect
from .forms import FornecedorForm
from django.db import IntegrityError
from django.utils.translation import gettext as _


def mostrar_formulario(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obrigado')
    else:
        form = FornecedorForm()
    return render(request, 'index.html', {'form': form})

def mostrar_obrigado(request):
    return render(request, 'obrigado.html')
