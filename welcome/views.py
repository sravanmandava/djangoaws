from django.shortcuts import render
from django.http import HttpResponse
from welcome.models import Name

# Create your views here.

def hello(request,name):
    return render(request,"hello.html",{"name":name})

    #return HttpResponse("<b> Hello "+ name +"</b>")

def saveToDb(request,name):
    Name.objects.create(name=name)
    count = Name.objects.count()
    return HttpResponse("<h2> You've inserted a name successfully </h2> <br> count = " + str(count))


def index(request):
    return HttpResponse("<h2> You've reached the HomePage page </h2>")
