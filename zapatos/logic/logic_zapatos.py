from ..models import Zapato

def get_zapatos():
    queryset = Zapato.objects.all()
    return (queryset)

def create_zapato(form):
    zapato = form.save()
    zapato.save()
    return ()

def delete_zapato(request):
    queryset = Zapato.objects.get(pk=2).delete()
    return (queryset)