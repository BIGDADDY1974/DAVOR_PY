from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("</br>"
                        "</br>"
                        "</br>"
                        "<h1><strong><center>HEY! THERE , THIS IS DAVOR SVILAR</center></strong></h2>"
                        "<h1><strong><center><font color='red'>POWERED DJANGO PAGE svilar.pythonanywhere.com !!!</font></center></strong></h2>")

