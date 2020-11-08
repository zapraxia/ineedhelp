# Generated by Django 3.1.3 on 2020-11-08 08:09

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('community', '0002_auto_20201107_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='discord_username',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='skype_link',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                                                   null=True),
        ),
        migrations.AlterField(
            model_name='correspondence',
            name='name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='correspondence',
            name='subject',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='university',
            name='description',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=254),
        ),
    ]