
from backend.api.models import EndPoint, ClassifierAlgorithm


class ClassifierRegistry:
    def __init__(self):
        self.classifiers = {}

    def register(self, endpoint_name, algorithm_object, algorithm_name, algorithm_description):

        endpoint_object, _ = EndPoint.objects.get_or_create(name=endpoint_name)

        created_algorithm, _ = ClassifierAlgorithm.objects.get_or_create(
            name=algorithm_name, description=algorithm_description, endpoint=endpoint_object)

        self.classifiers[created_algorithm.id] = algorithm_object
