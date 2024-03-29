import json
import requests

from rest_framework import viewsets
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.decorators import action
from backend.api.models import ClassifierAlgorithm, EndPoint, Request
from backend.api.serializers import ClassifierAlgorithmSerializer, EndpointSerializer, RequestSerializer
from backend.wsgi import registry
from django.http import JsonResponse
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
    
    @action(detail=False, methods=['get'], url_path='last-requests')
    def last_requests(self, request, pk=None):
        
        requests = Request.objects.all().order_by('-created_at')[:5]
        return Response(RequestSerializer(requests, many=True).data)

class PredictionView(views.APIView):
    def post(self, request, endpoint_name, format=None):
        data = request.data.copy()
        
        classifier = ClassifierAlgorithm.objects.filter(endpoint__name=endpoint_name)
        id = data.pop('rut', None)
        name = data.pop('name', None)
        if len(classifier) == 0:
            return Response(
                {"status": "Error", "message": "Classifier algorithm is not available at the given endpoint"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        classifier_object = registry.classifiers[classifier[0].id]
        # adding 2 options, treatment with trastuzumab and treatment with pertuzumab and trastuzumab
        data_schema_t = data.copy()
        data_schema_t.update({"esquema": 0})
        data_schema_tp = data.copy()
        data_schema_tp.update({"esquema": 1})
     
        prediction_scheme_t = classifier_object.make_prediction(data_schema_t)
        prediction_scheme_tp = classifier_object.make_prediction(data_schema_tp)
        prediction = {"name":data["nombre"],"age":data["edad"],"t_scheme":prediction_scheme_t, "tp_scheme":prediction_scheme_tp}
        request = Request(input_data=json.dumps(data), 
                          response_data=prediction, 
                          feedback_response="",
                          endpoint=classifier[0].endpoint,
                        #   patient_id=id,
                        # patient_name=name
                          )
        request.save() 
       
        return Response(prediction, status=status.HTTP_200_OK)
    
class ProxyView(views.APIView):
    def post(self, request):
        data = request.data.copy()
        
        url = data.get('url')
        method = data.get('method')
        headers = data.get('headers')
        data = data.get('data')
       
    
        response = requests.request(method, url, headers=headers, data=json.dumps(data))

     
        return JsonResponse(response.json(), safe=False)

