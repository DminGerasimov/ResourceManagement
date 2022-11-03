from usercloud.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  class Meta:
        model = User
        exclude = ['password']


class UserRegister(serializers.ModelSerializer):
  class Meta:
        model = User
        fields = '__all__'
