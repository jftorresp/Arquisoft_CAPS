from django.http import HttpResponse
from django.shortcuts import render

def title_page(request):
    return render(request, 'title_page.html')