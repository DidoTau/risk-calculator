from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from api.models import ClassifierAlgorithm, EndPoint, Request
from api.serializers import ClassifierAlgorithmSerializer, EndpointSerializer, RequestSerializer


class ClassifierAlgorithmViewSet(viewsets.ModelViewSet):
    queryset = ClassifierAlgorithm.objects.all()
    serializer_class = ClassifierAlgorithmSerializer


class EndpointViewSet(
    viewsets.ModelViewSet
):
    serializer_class = EndpointSerializer
    queryset = EndPoint.objects.all()
    
class RequestViewSet(viewsets.ModelViewSet
):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()