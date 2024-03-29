from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/<str:category_name>/', views.CategoryGamesView.as_view(), name='category'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('game/<int:game_id>/', views.GameView.as_view(), name='game'),
    path('search-game/', views.SearchGameView.as_view(), name='search_game'),
    path('delete-game/<int:pk>/', views.GameFromCartDeleteView.as_view(), name='cart-delete-game'),
    path('place-an-oder/',views.OrderWizardView.as_view(), name='place_an_order'),
    path('contact/',views.ContacView.as_view(),name='contact'),
    path('order-completed/',views.OrderCompleted.as_view(), name='order_completed')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)