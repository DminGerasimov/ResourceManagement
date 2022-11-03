from usercloud.models import User
from usercloud.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.renderers import JSONRenderer

class UserView(viewsets.ViewSet):

    def retrieve(self, request, pk=None, format=None):
        queryset = User.objects.all()
        # Извлекаем get - параметры для выборки пользователя из БД
        userid = self.request.query_params.get('id')
        if userid is not None:
            user = get_object_or_404(queryset, pk=userid)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        content = {"code 400": "bad request"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(viewsets.ViewSet):

    serializer_class = UserSerializer
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        content = {"code 400": "bad request"} #=serializer.errors
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def dataValidating(serializer.data):
        if re.fullmatch(r'\d{11}',serializer.data['phone']):
            return True

        pass