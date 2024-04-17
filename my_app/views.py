from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Python, Topic
from .serializers import TopicSerializer, TopicDetailSerializer
from rest_framework import status, viewsets, permissions
from rest_framework.generics import DestroyAPIView

from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class TopicListAPIView(ListAPIView):
    queryset = Topic.objects
    serializer_class = TopicSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        if 'keyword' in self.request.query_params:
            return Topic.objects.filter(topic_name__icontains=self.request.query_params['keyword'])
        return Topic.objects.all()


class TopicDetailAPIView(RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer


class TopicCreateAPIView(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    permission_classes = [IsAuthenticated]



class TopicUpdateAPIView(UpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super().patch(request, *args, **kwargs)


class TopicDeleteAPIView(DestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return Response()



class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
