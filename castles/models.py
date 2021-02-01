from django.db import models


class Castle(models.Model):
    castlesName = models.CharField(max_length=100, blank=True, default='')
    prefectureName = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
