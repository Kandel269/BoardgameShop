from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/<str:category_name>/', views.CategoryGamesView.as_view(), name='category'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('game/<int:game_id>/', views.GameView.as_view(), name='game')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)