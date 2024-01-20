from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(PersonalData)
admin.site.register(Payment)
admin.site.register(Delivery)