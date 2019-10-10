from django.urls import path, include
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('compraslist/', views.compra_list),
    path('comprascreate/', csrf_exempt(views.compra_create), name='compraCreate'),
    url(r'^compradetail/(?P<id>\d+)$', views.compra_detail),
]