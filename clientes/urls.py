from django.urls import path, include
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('clientescreate/', csrf_exempt(views.cliente_create)),
]