from rest_framework.generics import CreateAPIView

import users.serializers


class RegisterAPIView(CreateAPIView):
    serializer_class = users.serializers.UserSerializer

    def perform_create(self, serializer):
        serializer.save()
