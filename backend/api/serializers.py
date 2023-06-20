from rest_framework import serializers
from backend.api.models import ClassifierAlgorithm, EndPoint, Request


class ClassifierAlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifierAlgorithm
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
        
class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoint
        fields = '__all__'
        