from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('models', views.ModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]