from rest_framework import serializers

from api.models import Model


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model
        fields = ["id", "label"]