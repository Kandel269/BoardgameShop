from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from Shop.models import PersonalData


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class EditPersonalDataForm(forms.ModelForm):
    fist_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    e_mail_address = forms.EmailField(label="E-mail", max_length=255)
    class Meta:
        model = PersonalData
        fields = ['postal_code','house_number','local_number','street']


