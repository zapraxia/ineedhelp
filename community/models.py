from annoying import fields
from django.contrib.auth import get_user_model
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "universities"


class Program(models.Model):
    university = models.ForeignKey(University, related_name="programs", on_delete=models.CASCADE)
    members = models.ManyToManyField(get_user_model(), related_name="programs")

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = fields.AutoOneToOneField(get_user_model(), on_delete=models.CASCADE)

    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


class Correspondence(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    content = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
