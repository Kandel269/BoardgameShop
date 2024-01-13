from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from Shop.models import PersonalData # noqa


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class EditPersonalDataForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}))
    e_mail_address = forms.EmailField(label="E-mail", max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}))
    class Meta:
        model = PersonalData
        fields = ['postal_code','house_number','local_number','street']
        widgets = {
            'postal_code': forms.TextInput(attrs={'placeholder': ''}),
            'house_number': forms.TextInput(attrs={'placeholder': ''}),
            'local_number': forms.TextInput(attrs={'placeholder': ''}),
            'street': forms.TextInput(attrs={'placeholder': ''}),
        }

