from django.db import models
from django.contrib.auth import get_user_model
from annoying import fields


class University(models.Model):
    name = models.CharField(max_length=255)


class Program(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, related_name="programs", on_delete=models.CASCADE)


class Profile(models.Model):
    user = fields.AutoOneToOneField(get_user_model(), on_delete=models.CASCADE)

    description = models.CharField(max_length=255, blank=True)
