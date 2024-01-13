from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('account/', views.AccountPage.as_view(), name='account'),
    path('personal-data/', views.PersonalData.as_view(), name='personal_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)