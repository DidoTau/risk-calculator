from django.test import TestCase

# import DSGDClassifier
from backend.api.classifiers.dsgd import DSGDClassifier
from backend.api.classifiers.registry import ClassifierRegistry

# Create your tests here.


class ClassifierTests(TestCase):
    def test_dsgd(self):
        input_data = {
            'edad': 50,
            'imc': 25,
            'status_menop_al_dg': 'MENOPAUSICA',
            'ct': 'cT1',
            'cn': 'cN0',
            'etapa': 'I',
            'axila_en_eco': 0,
            'tipo_histologico': 'CDI',
            're': 80,
            'rp': 80,
            'ki67': 10,
            'relacion_her_2_cen': 2,
            'n°_de_copias': 3,
            'perfil_molecular': 'Luminal_Her2',
            'esquema': 0
        }

        dsgd_model = DSGDClassifier()
        dsgd_model.load_rules()
        prediction = dsgd_model.make_prediction(input_data)

        self.assertEqual('NO pCR', prediction['label'])

    def test_registry(self):

        registry = ClassifierRegistry()
        endpoint_name = 'dsgd_classifier'
        algorithm_name = 'dsgd'
        algorithm_object = DSGDClassifier()
        algorithm_description = 'dsgd classifier'

        self.assertEqual(len(registry.classifiers), 0)
        registry.register(endpoint_name, algorithm_object,
                          algorithm_name, algorithm_description)

        self.assertEqual(len(registry.classifiers), 1)
