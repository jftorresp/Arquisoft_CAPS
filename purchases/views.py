from django.shortcuts import render, get_object_or_404
from .forms import PurchaseForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .logic.logic_purchase import create_purchase, get_purchases
from django.urls import reverse
from .models import Purchase

# Create your views here.

def purchase_list(request):
    purchases = get_purchases()
    context = {
        'purchase_list': purchases
    }
    return render(request, 'purchases/purchaseList.html', context)

def purchase_create(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            create_purchase(form)
            messages.add_message(request, messages.SUCCESS, 'Compra creada exitosamente')
            return HttpResponseRedirect(reverse('purchaseCreate'))
        else:
            print(form.errors)
    else:
        form = PurchaseForm()

    context = {
        'form': form,
    }

    return render(request, 'purchases/purchaseCreate.html', context)

def purchase_detail(request, id=None):

    purchase = get_object_or_404(Purchase, id=id)
    
    context= {'purchase': purchase,
              }
    
    return render(request, 'purchases/purchaseDetail.html', context)
