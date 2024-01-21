from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from . import forms
from Shop.models import Cart, PersonalData # noqa




class LoginPage(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request,self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, self.template_name)

class RegisterPage(View):
    template_name = 'register.html'

    def get(self, request):
        form = forms.CreateUserForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account was created for' + user.username)
            cart = Cart(user=user)
            cart.save()
            personal_data = PersonalData(user=user)
            personal_data.save()
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, self.template_name, context)

class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class AccountPage(View):
    template_name = 'account.html'
    def get(self, request):
        return render(request,self.template_name)

class PersonalDataView(View):
    template_name = 'personal_data.html'


    def get(self, request):
        user = request.user
        personal_data = get_object_or_404(PersonalData, user=user)
        user_data = {'first_name': user.first_name,
                     'last_name': user.last_name,
                     'e_mail_address': user.email,
                     'city': personal_data.city,
                     'postal_code': personal_data.postal_code,
                     'house_number': personal_data.house_number,
                     'local_number': personal_data.local_number,
                     'street': personal_data.street}
        form = forms.EditPersonalDataForm(initial=user_data)
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = forms.EditPersonalDataForm(request.POST)
        if form.is_valid():
            user = request.user

            city_value = form.cleaned_data['city']
            postal_code_value = form.cleaned_data['postal_code']
            house_number_value = form.cleaned_data['house_number']
            local_number_value = form.cleaned_data['local_number']
            street_value = form.cleaned_data['street']
            personal_data = get_object_or_404(PersonalData, user=user)
            personal_data.city = city_value
            personal_data.postal_code = postal_code_value
            personal_data.house_number = house_number_value
            personal_data.local_number = local_number_value
            personal_data.street = street_value
            personal_data.save()

            first_name_value = form.cleaned_data['first_name']
            last_name_value = form.cleaned_data['last_name']
            e_mail_value = form.cleaned_data['e_mail_address']
            user.email = e_mail_value
            user.last_name = last_name_value
            user.first_name = first_name_value
            user.save()
            return redirect('home')
        else:
            context = {'form': form}
            return render(request, self.template_name, context)
