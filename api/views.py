from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ModelSerializer
from api.models import Model


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer