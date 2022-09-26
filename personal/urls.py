from rest_framework import routers
from .api import PersonalViewSet

router = routers.DefaultRouter()

router.register('api/personal', PersonalViewSet, 'personal')

urlpatterns = router.urls

