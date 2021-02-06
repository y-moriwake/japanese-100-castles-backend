from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Castle, Attribute
from .serializer import CastleSerializer


class TopCastleViewSet(ReadOnlyModelViewSet):
    queryset = Castle.objects.order_by('id')
    serializer_class = CastleSerializer


class NationalTreasureViewSet(ReadOnlyModelViewSet):
    queryset = Castle.objects.filter(attribute__is_national_treasure=True)
    serializer_class = CastleSerializer


class ExistenceViewSet(ReadOnlyModelViewSet):
    queryset = Castle.objects.filter(attribute__is_existence=True)
    serializer_class = CastleSerializer
