from rest_framework import serializers
from rest_framework.authtoken.admin import User

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
