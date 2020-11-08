# Generated by Django 3.1.3 on 2020-11-08 09:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0005_auto_20201108_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='programs', to=settings.AUTH_USER_MODEL),
        ),
    ]