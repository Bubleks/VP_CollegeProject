from django.contrib import admin

from .models import Title, Genre, Category, Platform, Catalogue, Item, Supplier, Shipping, Order

admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(Catalogue)

#
#
#

admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Shipping)
admin.site.register(Order)