from rest_framework import serializers

from api.models import Model, QualElement, QuantElement, Layout, QualElementPosition, QuantElementPosition, Connection


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    default_layout = serializers.PrimaryKeyRelatedField(queryset=Layout.objects.all(), required=False)

    class Meta:
        model = Model
        fields = ["id", "label", "default_layout"]



class LayoutSerializer(serializers.HyperlinkedModelSerializer):
    model = serializers.PrimaryKeyRelatedField(queryset=Model.objects.all())

    class Meta:
        model = Layout
        fields = ["id", "label", "model", ]


class QualElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QualElement
        fields = ["id", "label"]


class QualElementPositionSerializer(serializers.HyperlinkedModelSerializer):
    element = QualElementSerializer(many=False, read_only=True)
    class Meta:
        model = QualElementPosition
        fields = ["id", "x", "y", "element", "layout_id"]


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    to_element = serializers.PrimaryKeyRelatedField(queryset=QualElement.objects.all())
    from_element = serializers.PrimaryKeyRelatedField(queryset=QualElement.objects.all())
    class Meta:
        model = Connection
        fields = ["id", "from_element", "to_element"]