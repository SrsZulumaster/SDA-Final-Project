import wikipedia
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from spellchecker import SpellChecker

from SmartApp.forms import InputForm, OutputForm


def index(request):
    if request.method == "GET":
        form = InputForm(request.GET)
        if form.is_valid():
            return output(request)
    else:
        form = InputForm()
    return render(request, "text_input.html", {"form": form})


def output(request):
    content = request.GET.get('text_input')
    punctuations = request.GET.get('punctuations')
    upper = request.GET.get('upper')
    lower = request.GET.get('lower')
    removespace = request.GET.get("removeSpace")
    removeline = request.GET.get("spellCheck")
    charAmount = request.GET.get('countChars')
    summary = request.GET.get('summary')
    removeStop = request.GET.get('removeStop')
    context = stringLogic(punctuations, upper, lower, removespace, removeline,
                           charAmount, summary, removeStop, content)

    return render(request, "text-output.html", {"form": context[0],
                                                "head": context[1]})


def stringLogic(punctuations, upper, lower, removespace, removeline, charAmount, summary, removeStop, content):
    heading = "You did not select anything"
    if summary == "on":
        content = makeSummary(content)
        heading= "Your word summary is:"

    if punctuations == "on":
        content = punctuationsRemove(content)
        heading = "Your text without extra punctuations:"

    if upper == "on":
        content = makeUpper(content)
        heading = "Your text in uppercase:"

    if lower == "on":
        content = makeLower(content)
        heading = "Your text in lowercase:"

    if removespace == "on":
        content = removeExtraSpace(content)
        heading = "Your text without extra spaces"

    if removeline == "on":
        content = removeNewLine(content)
        heading = "Your text without extra lines"

    if charAmount == "on":
        content = countCharAmount(content)
        heading = "This is how many characters you text has:"

    if removeStop == "on":
        content = removeWordSTOP(content)
        heading= "Your text without Stop keyword is:"

    return content, heading


def punctuationsRemove(text_input: str):
    text_output = text_input.replace(".", "")
    return text_output


def makeUpper(text_input: str):
    text_output = text_input.upper()
    return text_output


def makeLower(text_input: str):
    text_output = text_input.lower()
    return text_output


def removeNewLine(text_input: str):
    text_output = text_input.strip()
    return text_output


def removeExtraSpace(text_input: str):
    while '  ' in text_input:
        text_input = text_input.replace('  ', ' ')

    text_output = text_input
    return text_output


def countCharAmount(text_input: str):
    text_output = len(text_input)
    return text_output


def checkSpelling(text_input: str):
    spell = SpellChecker()
    text_output = spell.unknown(text_input)
    return text_output


def makeSummary(text_input: str):
    text_output = wikipedia.summary(text_input)
    return text_output


def removeWordSTOP(text_input: str):
    text_input = text_input.replace("stop", "")
    text_input = text_input.replace("Stop", "")
    text_output = text_input.replace("STOP", "")
    return text_output
