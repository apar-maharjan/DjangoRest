from rest_framework import serializers
from rest_framework.authtoken.admin import User

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            confirm_password = validated_data.pop('confirm_password')
            # user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
            # user.set_password(validated_data.get('password'))
            # user.save()
            user = User.objects.create_user(**validated_data)
            return user

        def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError('Passwords must match')
            return data

