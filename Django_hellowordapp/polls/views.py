from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    "permite generar una vista"
    return HttpResponse("Hola Joan")