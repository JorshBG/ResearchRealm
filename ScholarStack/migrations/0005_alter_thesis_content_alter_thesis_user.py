# Generated by Django 5.0.3 on 2024-03-25 02:37

import ScholarStack.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarStack', '0004_remove_thesis_url_alter_thesis_content'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='content',
            field=models.FileField(unique=True, upload_to=ScholarStack.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='user',
            field=models.ForeignKey(db_column='author', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
