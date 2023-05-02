from django.shortcuts import render
from rest_framework import viewsets
from api.models import ClassifierAlgorithm
from api.serializers import ClassifierAlgorithmSerializer


class ClassifierAlgorithmViewSet(viewsets.ModelViewSet):
    queryset = ClassifierAlgorithm.objects.all()
    serializer_class = ClassifierAlgorithmSerializer
