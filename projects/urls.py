from rest_framework import routers
from .api import ProjecViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjecViewSet, 'projects')

urlpatterns = router.urls