from django.contrib import admin

from .models import Castle


@admin.register(Castle)
class Castle(admin.ModelAdmin):
    pass
