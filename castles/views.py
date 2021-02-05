from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import CastleMst
from .serializer import CastleSerializer


class CastleViewSet(ReadOnlyModelViewSet):
    queryset = CastleMst.objects.order_by('id')
    serializer_class = CastleSerializer
