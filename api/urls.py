from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.viewsets import DataViewset

router_v1 = DefaultRouter()

router_v1.register('data', DataViewset)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
