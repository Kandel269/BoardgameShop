from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *

class HomeView(View):
    def get(self, request):
        games = Game.objects.all().order_by('-published_date')
        context = {'games': games}
        return render(request,'home.html',context)

class CategoryGamesView(View):
    template_name = 'selected_category_games.html'

    def get(self, request, *args, **kwargs):
        category_name = kwargs.get('category_name')
        category = get_object_or_404(Category, name=category_name)
        games = Game.objects.filter(categories=category)

        context = {'category': category, 'games': games}
        return render(request,self.template_name,context)

class CartView(View):
    template_name = 'cart.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
