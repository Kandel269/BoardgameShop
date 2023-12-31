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

        # Prosty warunek sprawdzający, czy obraz ma inny rozmiar niż docelowy
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

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game, through='OrderItem')
    ordered_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

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
        return f'{self.quantity} x {self.game.title} in cart'
