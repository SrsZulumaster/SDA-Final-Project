from django import forms


class InputForm(forms.Form):
    text_input = forms.CharField(label="text_input", widget=forms.TextInput())
    switch1 = forms.BooleanField(required=False)
    switch2 = forms.BooleanField(required=False)
    switch3 = forms.BooleanField(required=False)
    switch4 = forms.BooleanField(required=False)
    switch5 = forms.BooleanField(required=False)
    switch6 = forms.BooleanField(required=False)
