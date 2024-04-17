from django.urls import path
from rest_framework import routers

from app_python.views import TopicViewSet

router = routers.DefaultRouter()
router.register(r'', TopicViewSet, 'topic')

urlpatterns = router.urls
