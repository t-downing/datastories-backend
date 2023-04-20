from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ModelSerializer, QualElementSerializer
from api.models import Model, QualElement, QuantElement, Layout, QualElementPosition, QuantElementPosition, Connection


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class QualElementViewSet(viewsets.ModelViewSet):
    queryset = QualElement.objects.all()
    serializer_class = QualElementSerializer