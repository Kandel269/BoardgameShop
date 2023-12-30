from .models import Cart, CartItem

def count_cart_items(request):
    cart_item_count = 0
    user = request.user

    if request.user.is_authenticated:
        games = user.cart.games.all()
        for game in games:
            cart_item = CartItem.objects.filter(cart = user.cart, game= game).first()
            cart_item_count += cart_item.quantity
    return {'cart_item_count': cart_item_count}