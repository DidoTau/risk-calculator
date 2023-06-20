import json

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework import mixins
from backend.api.models import ClassifierAlgorithm, EndPoint, Request
from backend.api.serializers import ClassifierAlgorithmSerializer, EndpointSerializer, RequestSerializer
from backend.wsgi import registry

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
    
class PredictionView(views.APIView):
    def post(self, request, endpoint_name, format=None):
        
        classifier = ClassifierAlgorithm.objects.filter(endpoint__name=endpoint_name)
        id = request.data.pop('rut', None)
        name = request.data.pop('name', None)
        if len(classifier) == 0:
            return Response(
                {"status": "Error", "message": "Classifier algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        
        classifier_object = registry.classifiers[classifier[0].id]
        prediction = classifier_object.make_prediction(request.data)
        request = Request(input_data=json.dumps(request.data), 
                          response_data=prediction, 
                          feedback_response="",
                          endpoint=classifier[0].endpoint,
                        #   patient_id=id,
                        # patient_name=name
                          )
        request.save() 
        return Response(prediction)