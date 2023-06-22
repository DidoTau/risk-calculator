from django.db import models

from .. import utils

class BaseModel(models.Model):
    
    id = models.CharField(
        ('ID'),
        db_index=True,
        primary_key=True,
        max_length=8,
        unique=True,
        default=utils.get_new_id,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
 
    class Meta:
        abstract = True
    
    
    
class EndPoint(BaseModel):
    '''
    This model represents a registered endpoint associated with a registered classifier algorithm.

    Atributes:
        name (str): The name of the endpoint.
        
    '''

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    


class ClassifierAlgorithm(BaseModel):
    '''
    This model represents a registered classifier algorithm.

    Atributes:
        name (str): The name of the algorithm.
        description (str): A brief description of the algorithm.
        created_at (datetime): The date and time of the creation of the algorithm.
        endpoint (EndPoint): The endpoint to access the algorithm.
    '''

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    
    endpoint = models.ForeignKey(EndPoint,
                                 related_name='classifier_algorithms',
                                 on_delete=models.CASCADE,
                                 null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classifier_algorithm'


class Request(BaseModel):
    '''
    This model represents a request to an endpoint.

    Atributes:
        
        patient_id (str): The rut or id of the patient that made the request.
        input_data (str): The input data of the request as JSON.
        response_data (str): The response data of the request as JSON.
        feedback_response (str): The feedback response of the request.
        endpoint (EndPoint): The endpoint that the request was made to.
    '''

    def __str__(self):
        return self.endpoint.name

    
    patient_id = models.CharField(max_length=255),
    patiend_name = models.CharField(max_length=255),
    input_data = models.CharField(max_length=10000)
    response_data = models.CharField(max_length=10000)
    feedback_response = models.CharField(
        max_length=10000, blank=True, null=True)
    endpoint = models.ForeignKey(EndPoint,
                                 related_name='requests',
                                 on_delete=models.CASCADE)
