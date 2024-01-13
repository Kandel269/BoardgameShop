from django import forms

class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
