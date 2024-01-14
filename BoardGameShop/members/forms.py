from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from Shop.models import PersonalData # noqa


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class EditPersonalDataForm(forms.Form):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}), required=None)
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}),  required=None)
    e_mail_address = forms.EmailField(label="E-mail", max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}), required=None)

    postal_code = forms.CharField(label="Postal-code",max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}), required=None)
    house_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}),required=None)
    local_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}),required=None)
    street = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': ''}),required=None)

