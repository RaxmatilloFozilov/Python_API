from django.urls import path

from .views import TopicListAPIView,TopicDetailAPIView, TopicCreateAPIView, TopicUpdateAPIView, TopicDeleteAPIView, TopicViewSet

from django.urls import path, include
from rest_framework import routers
from .filters import TopicFilter
router = routers.DefaultRouter()
router.register(r'topics', TopicViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('delete/<int:pk>/', TopicDeleteAPIView.as_view()),
    path('update/<int:pk>/', TopicUpdateAPIView.as_view()),
    path('create/', TopicCreateAPIView.as_view()),
    path('<int:pk>/', TopicDetailAPIView.as_view()),
    path('', TopicListAPIView.as_view()),
]