from django.shortcuts import render, get_object_or_404
from .forms import ZapatoForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_zapatos import create_zapato, get_zapatos, delete_zapato
from .models import Zapato
from django.contrib.auth.decorators import login_required
from CAPS.auth0backend import getRole

# Create your views here.

@login_required
def zapato_list(request):
    role = getRole(request)
    if role == "Administrador" or role == "Cliente" or role == "Fabricante": 
        zapatos = get_zapatos()
        context = {
            'zapato_list': zapatos
        }
        return render(request, 'zapatos/zapatos.html', context)
    else:
        return HttpResponse("Usuario No Autorizado")

@login_required
def zapato_create(request):
    role = getRole(request)
    if role == "Administrador":
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

        return render(request,'zapatos/zapatoCreate.html', context)
    else:
        return HttpResponse("Usuario No Autorizado")

def zapato_delete(request):
    if request.method == 'DELETE':
        delete_zapato(request)

@login_required
def zapato_detail(request, id=None):
    role = getRole(request)
    if role == "Administrador" or role == "Cliente" or role == "Fabricante":
        zapato = get_object_or_404(Zapato, id=id)
        context= {'zapato': zapato,
             	 }
        return render(request, 'zapatos/zapatoDetail.html', context)
    else:
        return HttpResponse("Usuario No Autorizado")
