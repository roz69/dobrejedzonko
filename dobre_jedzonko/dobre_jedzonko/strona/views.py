from django.shortcuts import render
from django.http import Http404
from .models import Recipe

def glowna(request):
    recipes = Recipe.objects.all()
    return render(request, 'glowna.html', {'recipes': recipes})

