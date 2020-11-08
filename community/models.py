from annoying import fields
from django.contrib.auth import get_user_model
from django.db import models
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    YEAR = Choices(1, 2, 3, 4, 5)

    user = fields.AutoOneToOneField(get_user_model(), on_delete=models.CASCADE)

    description = models.CharField(max_length=254, blank=True)
    year = models.PositiveSmallIntegerField(choices=YEAR, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    discord_username = models.CharField(max_length=254, null=True, blank=True)
    facebook_link = models.CharField(max_length=254, null=True, blank=True)
    skype_username = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.user.username


class University(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "universities"


class Program(models.Model):
    university = models.ForeignKey(University, related_name="programs", on_delete=models.CASCADE)
    members = models.ManyToManyField(get_user_model(), related_name="programs", blank=True)

    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return f"{self.university} {self.name}"


class Correspondence(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    subject = models.CharField(max_length=254)
    content = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
