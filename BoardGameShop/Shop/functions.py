from Shop.models import CartItem, Cart
from django.shortcuts import get_object_or_404

def is_game_in_cart(cart, game):
    return cart.games.filter(id=game.id).exists()

def add_quantity(cart, game):
    cart_item = CartItem.objects.filter(cart = cart, game = game).first()
    cart_item.quantity += 1
    cart_item.save()
    return

def get_cart(request):
    user = request.user
    cart = get_object_or_404(Cart, user__id=user.id)
    return cart