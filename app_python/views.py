from rest_framework import viewsets, permissions

from my_app.models import Topic
from my_app.serializers import TopicDetailSerializer


class TopicPermission(permissions.BasePermission):

    def has_object_permission(self, request, view):
        if request.method == 'GET':
            return True

        return request.user.is_authenticated() and request.user


class TopicViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    permission_classes = [TopicPermission]
