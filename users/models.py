from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username


class EventModel(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class CollectionsModel(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name

class CategoryModel(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name
