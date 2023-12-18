from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    email = forms.EmailField(label="Your e-mail")