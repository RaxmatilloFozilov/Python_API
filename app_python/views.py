from rest_framework import viewsets

from my_app.models import Topic
from my_app.serializers import TopicDetailSerializer


class TopicViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
