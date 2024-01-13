from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from . import forms
from Shop.models import Cart




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

class PersonalData(View):
    template_name = 'personal_data.html'
    def get(self, request):
        form = forms.EditPersonalDataForm()
        context = {'form':form}
        return render(request, self.template_name, context)

