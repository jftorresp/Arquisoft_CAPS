from django.urls import path, include
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('compras/', views.zapato_list),
    path('zapatoscreate/', csrf_exempt(views.zapato_create), name='zapatoCreate'),
    path('zapatosdelete/', csrf_exempt(views.zapato_delete)),
    url(r'^zapatodetail/(?P<id>\d+)$', views.zapato_detail),
]