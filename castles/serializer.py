from rest_framework import serializers

from .models import Castle, Attribute


class CastleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Castle
        fields = ('id', 'name', 'prefecture', 'address', 'description')
