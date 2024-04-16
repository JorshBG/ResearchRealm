from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from ScholarStack.models import Thesis
from .serializers import UserSerializer, ThesisSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
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
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_thesis(request):
    serializer = ThesisSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def index_thesis(request):
    thesis = Thesis.objects.all()
    serializer = ThesisSerializer(thesis, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_thesis(request, id):
    thesis = get_object_or_404(Thesis, pk=id)
    serializer = ThesisSerializer(thesis, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_thesis(request, id):
    request.data['id'] = id
    serializer = ThesisSerializer(data=request.data)
    if serializer.is_valid():
        thesis = get_object_or_404(Thesis, pk=id)
        thesis.title = request.data['title']
        thesis.description = request.data['description']
        thesis.user = request.user
        thesis.content = request.data['content']
        thesis.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
