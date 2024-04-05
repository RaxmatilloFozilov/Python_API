from rest_framework import serializers

from .models import  Topic, Python


class TopicSerializer(serializers.ModelSerializer):
    topic_detail_url = serializers.SerializerMethodField(read_only=True, source='get_topic_url')

    class Meta:
        model = Topic
        fields = ['id', 'topic_name', 'topic_content', 'topic_banner','topic_detail_url']
        depth= 1

    def get_topic_detail_url(self, obj):
        return f"http://localhost:8000/api/v1/python{obj.id}"


class TopicDetailSerializer(serializers.ModelSerializer):
    # topic_genre_info = serializers.SerializerMethodField(read_only=True, source='get_topic_genre_info')

    class Meta:
        model = Topic
        fields = '__all__'
        depth = 1

    # def get_topic_content_info(self, obj):
    #     info={
    #         'topic_id': obj.topic_content,
    #         'topic_content': obj.topic_content.topic_content
    #     }
    #     return info
    #


