from rest_framework import serializers

from .models import CastleMst


class CastleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastleMst
        fields = ('id', 'name', 'prefecture', 'address', 'description')
