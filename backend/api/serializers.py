from rest_framework import serializers
from api.models import ClassifierAlgorithm


class ClassifierAlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifierAlgorithm
        fields = '__all__'
