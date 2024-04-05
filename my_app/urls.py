from django.urls import path

from .views import TopicListAPIView,TopicDetailAPIView, TopicCreateAPIView, TopicUpdateAPIView, TopicDeleteAPIView

urlpatterns = [
    path('delete/', TopicDeleteAPIView.as_view()),
    path('update/', TopicUpdateAPIView.as_view()),
    path('create/', TopicCreateAPIView.as_view()),
    path('<int:pk>/', TopicDetailAPIView.as_view()),
    path('', TopicListAPIView.as_view()),
]