from usercloud.models import User
from usercloud.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UserView(viewsets.ViewSet):

    def retrieve(self, request, pk=None, format=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
