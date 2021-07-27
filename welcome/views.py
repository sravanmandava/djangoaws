from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request,name):
    return render(request,"hello.html",{"name":name})

    #return HttpResponse("<b> Hello "+ name +"</b>")
