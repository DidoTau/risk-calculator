"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from backend.api.classifiers.dsgd import DSGDClassifier
from backend.api.classifiers.registry import ClassifierRegistry

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()

try:
    registry = ClassifierRegistry()
    dsgd = DSGDClassifier()
    dsgd.load_rules()
    registry.register(endpoint_name='dsgd_classifier', 
                      algorithm_object=dsgd, 
                      algorithm_name='dsgd', 
                      algorithm_description='Dempster Shafer Gradient Descent classifier')
    
except Exception as e:
    print("Exception while loading the classifier to the registry,", str(e))