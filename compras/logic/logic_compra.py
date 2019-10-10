from ..models import Compra

def create_compra(form):
    compra = form.save()
    compra.save()
    return ()

def get_compras():
    queryset = Compra.objects.all()
    return (queryset)