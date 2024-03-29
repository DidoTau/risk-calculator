"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from backend.api.views import ClassifierAlgorithmViewSet, EndpointViewSet, RequestViewSet, PredictionView, ProxyView


router = SimpleRouter()
router.register(r'classifier', ClassifierAlgorithmViewSet)
router.register(r'endpoints', EndpointViewSet)
router.register(r'requests', RequestViewSet, basename='requests')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/<str:endpoint_name>/predict/', PredictionView.as_view(), name='predict'),
    # proxy
    path('api/proxy/', ProxyView.as_view(), name='proxy'),
    
]