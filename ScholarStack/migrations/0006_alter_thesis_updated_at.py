# Generated by Django 5.0.3 on 2024-03-28 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarStack', '0005_alter_thesis_content_alter_thesis_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
