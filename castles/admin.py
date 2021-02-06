from django.contrib import admin

from .models import Castle, Attribute


@admin.register(Castle)
class Castle(admin.ModelAdmin):
    pass


@admin.register(Attribute)
class Attribute(admin.ModelAdmin):
    pass
