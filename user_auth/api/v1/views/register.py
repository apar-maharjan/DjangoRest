from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_auth.api.v1.serializers.register import UserRegisterSerializer


@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)