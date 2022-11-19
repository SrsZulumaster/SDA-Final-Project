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
    if punctuations == "on":
        return render(request, "text-output.html", {"form": punctuationsRemove(content),
                                                    "head": "Text Without Punctuations"})
    elif upper == "on":
        return render(request, "text-output.html", {"form": makeUpper(content),
                                                    "head": "Text In Capitals"})
    elif lower == "on":
        return render(request, "text-output.html", {"form": makeLower(content),
                                                    "head": "Text in Lowercase"})
    elif removespace == "on":
        return render(request, "text-output.html", {"form": removeExtraSpace(content),
                                                    "head": "Text with no extra spaces"})
    elif removeline == "on":
        return render(request, "text-output.html", {"form": removeNewLine(content),
                                                    "head": "Text without new line"})
    elif charAmount == "on":
        return render(request, "text-output.html", {"form": countCharAmount(content),
                                                    "head": "Your Text Length was:"})
    elif summary == "on":
        return render(request, "text-output.html", {"form": makeSummary(content),
                                                    "head": "Your Word Summary is:"})
    elif removeStop == "on":
        return render(request, "text-output.html", {"form": removeWordSTOP(content),
                                                    "head": "Your text without the word Stop"})
    else:
        return render(request, "text-output.html", {"form": content,
                                                    "head": "Your original text:"})


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
