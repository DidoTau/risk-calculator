import json

from rest_framework import serializers
from backend.api.models import ClassifierAlgorithm, EndPoint, Request
from django.utils import timezone

class ClassifierAlgorithmSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassifierAlgorithm
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
   
    date = serializers.SerializerMethodField()
    input_data = serializers.SerializerMethodField()
    response_data = serializers.SerializerMethodField()
    class Meta:
        model = Request
        fields = [ 'date','input_data', 'response_data' ]
    
    def get_date(self, instance):
        corrected_date = timezone.localtime(instance.updated_at)
       
        return corrected_date.strftime("%d-%m-%Y")
    
    def get_input_data(self, instance):
     
        return json.loads(instance.input_data)
    
    def get_response_data(self, instance):
        json_string = instance.response_data.replace("'", "\"")

        return json.loads(json_string)
class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoint
        fields = '__all__'
        