from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if user.is_active:
        if not user.check_password(request.data['password']):
            return Response({
                'message': 'Invalid password',
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(instance=user)
            return Response({
                'token': token.key,
                'user': serializer.data
            })
    else:
        return Response({
            'message': 'Inactive user'
        })


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = get_object_or_404(User, username=serializer.data['username'])
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


def handler404(request, *args, **kwargs):
    return render(request, 'pages/error/404.html')


def handler500(request, *args, **kwargs):
    return render(request, 'pages/error/404.html')

