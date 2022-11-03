from usercloud.models import User
from usercloud.serializers import UserSerializer, UserRegister
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from datetime import date, datetime


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

    serializer_class = UserRegister
    
    def create(self, request):
        serializer = UserRegister(data=request.data)
        if serializer.is_valid():
            birth = serializer.validated_data['birth']
            if (int((date.today() - birth).days / 365.2425) > 18):
                serializer.save()
                return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        content = {"code 400": "bad request or 18+ or user already exist"} #=serializer.errors
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(viewsets.ViewSet):

    def retrieve(self, request):
        login = request.data['login']
        password = request.data['password']
        queryset = User.objects.filter(login=login, password=password).values('id')
        if len(queryset):
            userid = {'id': queryset[0]['id']}
            return Response(userid)
        content = {"code 400": "bad request"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
