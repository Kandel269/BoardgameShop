from Shop.models import CartItem


def is_game_in_cart(cart, game):
    return cart.games.filter(id=game.id).exists()

def add_quantity(cart, game):
    cart_item = CartItem.objects.filter(cart = cart, game = game).first()
    cart_item.quantity += 1
    cart_item.save()
    return