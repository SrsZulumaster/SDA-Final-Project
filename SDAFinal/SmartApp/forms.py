from django import forms
from spellchecker import SpellChecker
import wikipedia


class InputForm(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control",
               "rows": "6"
                }))
    punctuations = forms.BooleanField(required=False, widget=)
    upper = forms.BooleanField(required=False)
    lower = forms.BooleanField(required=False)
    removeLine = forms.BooleanField(required=False)
    removeSpace = forms.BooleanField(required=False)
    countChars = forms.BooleanField(required=False)
    spellCheck = forms.BooleanField(required=False)
    summary = forms.BooleanField(required=False)
    removeStop = forms.BooleanField(required=False)

    def __str__(self):
        return self.text_input


class OutputForm(forms.Form):
    text_output = forms.Textarea()
