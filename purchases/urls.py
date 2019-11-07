from django.urls import path, include
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('purchaseslist/', views.purchase_list),
    path('purchasescreate/', csrf_exempt(views.purchase_create), name='purchaseCreate'),
    url(r'^purchasesdetail/(?P<id>\d+)$', views.purchase_detail),
]