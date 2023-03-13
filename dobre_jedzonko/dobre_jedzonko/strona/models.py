from django.db import models
from .pathandrename import PathAndRename

class Recipe(models.Model):
    dish_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=PathAndRename('recipe/').wrapper)
    date_time = models.DateTimeField('date published')
    describe = models.TextField(max_length=4000)
    time_prepair = models.PositiveIntegerField()
    linkYT = models.URLField(max_length=500, blank=True)
    DUPA = [
        ('N', 'NOOB'),
        ('E', 'Łatwy'),
        ('M', 'Średni'),
        ('H', 'Trudny'),
        ('S', 'MasterChef'),
    ]
    difficulty = models.CharField(max_length=1, choices=DUPA, blank=True)
    def __str__(self):
        return self.dish_name


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_photo = models.ImageField(upload_to=PathAndRename('author/').wrapper)
    surname = models.CharField(max_length=50)
    social_IG = models.URLField(max_length=500, blank=True)
    social_SNAP = models.URLField(max_length=500, blank=True)
    social_FB = models.URLField(max_length=500, blank=True)
    social_PH = models.URLField(max_length=500, blank=True)
    social_OF = models.URLField(max_length=500, blank=True)
    recipes = models.ManyToManyField(Recipe, related_name='author', blank=True)
    def __str__(self):
        return self.author_name

