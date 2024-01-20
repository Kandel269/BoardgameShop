from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from formtools.wizard.views import SessionWizardView

from .models import *
from .functions import *
from .forms import *
from members.forms import EditPersonalDataForm # noqa


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

class OrderWizardView(SessionWizardView):
    form_list = [OrderDetailForm,EditPersonalDataForm,DeliveryForm,ConfirmOrder]
    template_name = "place_an_order.html"

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        user = self.request.user

        if step == '1':
            personal_data = get_object_or_404(PersonalData, user=user)
            initial.update({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'e_mail_address': user.email,
                'postal_code': personal_data.postal_code,
                'house_number': personal_data.house_number,
                'local_number': personal_data.local_number,
                'street': personal_data.street,
            })

        return self.initial_dict.get(step, initial)

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        step = self.steps.current
        user = self.request.user

        if step == '3':
            step_0_data = self.get_cleaned_data_for_step('0')
            step_1_data = self.get_cleaned_data_for_step('1')
            step_2_data = self.get_cleaned_data_for_step('2')

            payment_name = step_0_data.get('payment')
            payment = get_object_or_404(Payment, name=payment_name)
            context['payment'] = payment

            delivery_name = step_2_data.get('delivery')
            delivery = get_object_or_404(Delivery, name=delivery_name)
            context['delivery'] = delivery

            context['step_1_data'] = {
                'first_name': step_1_data.get('first_name'),
                'last_name': step_1_data.get('last_name'),
                'e_mail_address': step_1_data.get('e_mail_address'),
                'postal_code': step_1_data.get('postal_code'),
                'house_number': step_1_data.get('house_number'),
                'local_number': step_1_data.get('local_number'),
                'street': step_1_data.get('street')
            }

            price_games = 0
            if user.is_authenticated:
                games_dict = get_quantity(user)
                for game, describe in games_dict.items():
                    price_games += describe[1]
                context['price_games'] = price_games

            total_price = price_games + delivery.price
            context['total_price'] = total_price

        return context

    def done(self, form_list, **kwargs):
        user = self.request.user
        step_0_data = self.get_cleaned_data_for_step('0')
        step_1_data = self.get_cleaned_data_for_step('1')
        step_2_data = self.get_cleaned_data_for_step('2')

        delivery_address = DeliveryAddress(
            first_name=step_1_data.get('first_name'),
            last_name=step_1_data.get('last_name'),
            e_mail=step_1_data.get('e_mail_address'),
            postal_code=step_1_data.get('postal_code'),
            house_number=step_1_data.get('house_number'),
            local_number=step_1_data.get('local_number'),
            street=step_1_data.get('street'),
        )
        delivery_address.save()

        payment_name = step_0_data.get('payment')
        payment = get_object_or_404(Payment, name=payment_name)
        delivery_name = step_2_data.get('delivery')
        delivery = get_object_or_404(Delivery, name=delivery_name)

        order = Order(user=user, delivery_address=delivery_address, payment=payment, delivery=delivery)

        price_games = 0
        if user.is_authenticated:
            games_dict = get_quantity(user)
            list_order_item = []
            for game, describe in games_dict.items():
                price_games += describe[1]
                order_item = OrderItem(game=game,order = order, quantity=describe[0])
                list_order_item.append(order_item)
                game.stock -= describe[0]
                game.save()
            cart = get_object_or_404(Cart, user=user)
            cart_items = CartItem.objects.filter(cart=cart)
            cart_items.delete()

        total_price = price_games + delivery.price
        order.total_price = total_price
        order.save()
        for item in list_order_item:
            item.save()

        return redirect('order_completed')

class ContacView(View):
    template_name = "contact.html"

    def get(self,request):
        return render(request, self.template_name)

class OrderCompleted(View):
    template_name = 'order_completed.html'

    def get(self,request):
        return render(request,self.template_name)