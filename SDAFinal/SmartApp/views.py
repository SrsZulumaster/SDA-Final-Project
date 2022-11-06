from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from SmartApp.forms import InputForm


def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            text_input = form.text_input
            if form.switch1 == "on":
                stringy= "asdad"
                stringy= stringy.upper()
                text_input = text_input.upper()
                return output(request, text_input)
    else:
        form = InputForm()
    return render(request, "text_input.html", {"form": form})


def output(request, text):
    return render(request, template_name="text-output.html")
