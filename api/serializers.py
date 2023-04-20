from rest_framework import serializers

from api.models import Model, QualElement, QuantElement, Layout, QualElementPosition, QuantElementPosition, Connection


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model
        fields = ["id", "label", "default_layout_id"]


class LayoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Layout
        fields = ["id", "label", "model_id"]


class QualElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QualElement
        fields = ["id", "label"]


class QualElementPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QualElementPosition
        fields = ["id", "x", "y", "element_id", "layout_id"]


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ["id", "from_element_id", "to_element_id"]