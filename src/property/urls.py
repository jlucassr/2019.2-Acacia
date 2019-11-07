from django.urls import path, include
from .viewsets import PropertyViewSet
from rest_framework import routers


app_name = 'property'

router = routers.SimpleRouter()
router.register(r'', PropertyViewSet, basename='property')

urlpatterns = [
    path('<int:pk_property>/trees/', include('tree.urls')),
] + router.urls
