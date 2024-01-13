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
                     'postal_code': personal_data.postal_code,
                     'house_number': personal_data.house_number,
                     'local_number': personal_data.local_number,
                     'street': personal_data.street}
        form = forms.EditPersonalDataForm(initial=user_data)
        context = {'form':form}
        return render(request, self.template_name, context)

