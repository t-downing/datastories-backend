from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from api.serializers import ModelSerializer, QualElementSerializer, LayoutSerializer, QualElementPositionSerializer, ConnectionSerializer
from api.models import Model, QualElement, QuantElement, Layout, QualElementPosition, QuantElementPosition, Connection


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class QualElementViewSet(viewsets.ModelViewSet):
    queryset = QualElement.objects.all()
    serializer_class = QualElementSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = {"id": ["in", "exact"]}


class LayoutViewSet(viewsets.ModelViewSet):
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ["model"]


class QualElementPositionViewSet(viewsets.ModelViewSet):
    queryset = QualElementPosition.objects.all()
    serializer_class = QualElementPositionSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ["layout_id"]


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    # filter_backends = (filters.DjangoFilterBackend, )
    # filterset_fields = {"id": ["in", "exact"]}