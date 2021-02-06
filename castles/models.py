from django.db import models


class Castle(models.Model):
    name = models.CharField(
        verbose_name='城名', max_length=100, blank=True, default='')
    prefecture = models.CharField(
        verbose_name='都道府県名', max_length=100, blank=True, default='')
    address = models.CharField(
        verbose_name='住所', max_length=1024, blank=True, default='')
    description = models.CharField(
        verbose_name='説明', max_length=1024, blank=True, default='')


class Attribute(models.Model):
    castle = models.OneToOneField(
        Castle, on_delete=models.CASCADE, primary_key=True, default=0, null=False)
    is_national_treasure = models.BooleanField()
    is_existence = models.BooleanField()
