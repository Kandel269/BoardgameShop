from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps


# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='game_images/')
    published_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        target_size = (300, 300)

        if img.size != target_size:
            img = img.resize(target_size)
            img.save(self.image.path)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)
    games = models.ManyToManyField(Game, related_name='categories', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class DeliveryAddress(models.Model):
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    e_mail = models.EmailField(default=None)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    local_number = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Delivery Address"
        verbose_name_plural = "Delivery Address"

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}  postal-code:{self.postal_code} house number:{self.house_number} local number:{self.local_number} street:{self.street}"

class Payment(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='website_images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        target_size = (300, 300)

        if img.size != target_size:
            img = img.resize(target_size)
            img.save(self.image.path)

    def __str__(self):
        return self.name

class Delivery(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='website_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        target_size = (300, 300)

        if img.size != target_size:
            img = img.resize(target_size)
            img.save(self.image.path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Delivery"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game, through='OrderItem', blank=True, null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.PROTECT, default=None)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT, default=None)
    delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return f"Order #{self.pk}"

class OrderItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.game.title}'

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game, through='CartItem')

    def __str__(self):
        return f'Cart for {self.user.username}'

class CartItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.game.title}'

class PersonalData(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=255, blank=True, null=True)
    local_number = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"username: {self.user.first_name} {self.user.last_name} postal-code:{self.postal_code} house number:{self.house_number} local number:{self.local_number} street:{self.street}"

    class Meta:
        verbose_name = "Personal Data"
        verbose_name_plural = "Personal Data"
