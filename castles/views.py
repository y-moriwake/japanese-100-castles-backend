from django.shortcuts import render
import django_filters
from rest_framework.viewsets import ModelViewSet

from .models import Castle
from .serializer import CastleSerializer


class CastleViewSet(ModelViewSet):
    queryset = Castle.objects.all()
    serializer_class = CastleSerializer
