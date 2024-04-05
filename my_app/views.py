from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Python, Topic
from .serializers import TopicSerializer, TopicDetailSerializer
from rest_framework import status
from rest_framework.generics import DestroyAPIView

# Create your views here.


class TopicListAPIView(ListAPIView):
    queryset = Topic.objects
    serializer_class = TopicSerializer


class TopicDetailAPIView(RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer


class TopicCreateAPIView(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer


class TopicUpdateAPIView(UpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    permission_classes = [IsAuthenticated]


# class TopicDeleteAPIView(DestroyAPIView):
#     queryset = Topic.objects.all()
#     serializer_class = TopicDetailSerializer
#
# def delete(self, request, *args, **kwargs):
#     instance = self.get_object()
#     self.perform_destroy(instance)
#     return Response(status=status.HTTP_204_NO_CONTENT)

class TopicDeleteAPIView(DestroyAPIView):
    queryset =Topic.objects.all()
    serializer_class =TopicDetailSerializer
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return Response()
