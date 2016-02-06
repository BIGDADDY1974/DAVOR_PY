from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>HELLO THERE GOOD LOOKING !!!</h1>")


# Create your views here.
