from ..models import Purchase

def create_purchase(form):
    purchase = form.save()
    purchase.save()
    return ()

def get_purchases():
    queryset = Purchase.objects.all()
    return (queryset)