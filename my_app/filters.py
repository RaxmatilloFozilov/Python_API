from rest_framework.filters import BaseFilterBackend
import coreapi

import django_filters
from .models import Topic


class TopicFilterBackend(BaseFilterBackend):

    def get_filters(self, request, view):
        fildes = [
            creapi.Field(
                name='name',
                location='query',
                required=False,
                type='string',
                description='Get',

            )
        ]
        return filter

    def filter_queryset(self, request, queryset, view):
        return queryset.filter()


class TopicFilter(django_filters.FilterSet):
    topic_name = django_filters.CharFilter(lookup_expr='exact')
    topic_subject = django_filters.CharFilter(lookup_expr='contains')
    topic_content = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Topic
        fields = ['topic_name', 'topic_subject', 'topic_content']
