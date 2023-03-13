from django.contrib import admin
from .models import Recipe, Author


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'dish_name']
    list_display_links = ['dish_name']
    search_fields = ['dish_name', 'date_time', 'time_prepair', 'difficulty']
    list_filter = ['date_time', 'time_prepair', 'difficulty']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name']
    list_display_links = ['author_name']
