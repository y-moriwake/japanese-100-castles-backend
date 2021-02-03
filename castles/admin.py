from django.contrib import admin

from .models import CastleMst


@admin.register(CastleMst)
class CastleMst(admin.ModelAdmin):
    pass
