from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from SmartApp.forms import InputForm


def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("output/")
    else:
        form = InputForm()
    return render(request, "text_input.html", {"form": form})


def output(request, get_input_on_post):
    return render(request, template_name="text-output.html")
