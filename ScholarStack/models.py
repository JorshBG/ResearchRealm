from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    date = datetime.now()
    year = date.year
    month = date.month
    return f'thesis/{instance.user.username}/{year}/{month}/{filename}'


class Thesis(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    content = models.FileField(upload_to=user_directory_path, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='author')
    likes = models.ManyToManyField(User, related_name='user_likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


