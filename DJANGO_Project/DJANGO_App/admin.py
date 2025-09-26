from django.contrib import admin

from .models import Title, Genre, Category, Platform, Catalogue

admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(Catalogue)
