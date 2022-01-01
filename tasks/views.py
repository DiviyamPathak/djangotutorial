from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import tasks
from django.urls import reverse




Tasks=["foo", "bar" , "qiz"] 

class NewTasksForm(forms.Form):
    task = forms.CharField(label="Add New Task")


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks":Tasks
    })

def add(request):
    

    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid:
            task = form.cleaned_data["task"]
            Tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks:add",{
            "forms": form
        })
    return render(request, "tasks/add.html", {
        "forms":NewTasksForm()
    })