from rest_framework import serializers

from .models import Castle


class CastleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Castle
        fields = ('id', 'castlesName', 'prefectureName', 'description')
