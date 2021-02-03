from django.db import models


class CastleMst(models.Model):
    id = models.IntegerField(primary_key=True, default=0, null=False)
    name = models.CharField(max_length=100, blank=True, default='')
    prefecture = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
