from django.shortcuts import render
from django.views import View
from .models import *

class HomeView(View):
    def get(self, request):
        games = Game.objects.all().order_by('-published_date')
        context = {'games': games}
        return render(request,'home.html',context)