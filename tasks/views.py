from django.shortcuts import render
from django.http import HttpResponse

import tasks

Tasks=["foo", "bar" , "qiz"] 


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks":Tasks
    })

def add(request):
    
    return render(request, "tasks/add.html")