from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

from ScholarStack.models import Thesis


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    email = serializers.EmailField(max_length=100, required=True, validators=[
        UniqueValidator(queryset=User.objects.all())
    ])

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ThesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thesis
        fields = [
            'id',
            'title',
            'description',
            'content',
            'user',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        thesis, created = Thesis.objects.get_or_create(**validated_data)
        if not created:
            thesis.title = validated_data['title']
            thesis.description = validated_data['description']
            thesis.content = validated_data['content']
            thesis.user = validated_data['user']
        return thesis
