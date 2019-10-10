from django.shortcuts import render, get_object_or_404
from .forms import ZapatoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_zapatos import create_zapato, get_zapatos, delete_zapato
from .models import Zapato

# Create your views here.

def zapato_list(request):
    zapatos = get_zapatos()
    context = {
        'zapato_list': zapatos
    }
    return render(request, 'zapatos/zapatos.html', context)

def zapato_create(request):
    if request.method == 'POST':
        form = ZapatoForm(request.POST)
        if form.is_valid():
            create_zapato(form)
            messages.add_message(request, messages.SUCCESS, 'Zapato creado exitosamente')
            return HttpResponseRedirect(reverse('zapatoCreate'))
        else:
            print(form.errors)
    else:
        form = ZapatoForm()

    context = {
        'form': form,
    }

    return render(request, 'zapatos/zapatoCreate.html', context)

def zapato_delete(request):
    if request.method == 'DELETE':
        delete_zapato(request)

def zapato_detail(request, id=None):

    zapato = get_object_or_404(Zapato, id=id)
    
    context= {'zapato': zapato,
              }
    
    return render(request, 'zapatos/zapatoDetail.html', context)

