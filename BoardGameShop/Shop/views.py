from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from .models import *
from .functions import *

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
        context = {}
        user = request.user
        if user.is_authenticated:
            games_dict = get_quantity(user)
            context['games_dict'] = games_dict

        return render(request, self.template_name, context)

class GameView(View):
    template_name = 'game.html'

    def get(self, request, *args, **kwargs):
        game_id = kwargs.get('game_id')
        game = get_object_or_404(Game, id=game_id)
        cart = get_cart(request)
        in_cart = is_game_in_cart(cart,game)
        context = {'game':game, 'in_cart':in_cart}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        game_id = request.POST.get('game_id')
        game = get_object_or_404(Game, id=game_id)
        cart = get_cart(request)
        if is_game_in_cart(cart, game):
            add_quantity(cart, game)
        else:
            cart.games.add(game)
        in_cart = is_game_in_cart(cart, game)
        context = {'game': game, 'in_cart':in_cart}
        return render(request, self.template_name,context)

class SearchGameView(View):
    template_name = 'search_game.html'

    def post(self, request, *args, **kwargs):
        find_game = request.POST.get('find_game')
        games = Game.objects.filter(title__icontains=find_game)
        context = {'games': games, 'find_game':find_game}
        return render(request, self.template_name, context)

class GameFromCartDeleteView(DeleteView):
    model = CartItem
    template_name = "cart_confirm_delete_product.html"
    success_url = reverse_lazy("cart")