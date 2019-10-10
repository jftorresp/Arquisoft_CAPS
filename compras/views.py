from django.shortcuts import render, get_object_or_404
from .forms import CompraForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .logic.logic_compra import create_compra, get_compras
from django.urls import reverse
from .models import Compra

# Create your views here.

def compra_list(request):
    compras = get_compras()
    context = {
        'compra_list': compras
    }
    return render(request, 'compras/compraList.html', context)

def compra_create(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            create_compra(form)
            messages.add_message(request, messages.SUCCESS, 'Compra creada exitosamente')
            return HttpResponseRedirect(reverse('compraCreate'))
        else:
            print(form.errors)
    else:
        form = CompraForm()

    context = {
        'form': form,
    }

    return render(request, 'compras/compraCreate.html', context)

def compra_detail(request, id=None):

    compra = get_object_or_404(Compra, id=id)
    
    context= {'compra': compra,
              }
    
    return render(request, 'compras/compraDetail.html', context)