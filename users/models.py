from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users_images/', null=True, blank=True)
    events = models.ManyToManyField('EventModel', blank=True)

    def __str__(self):
        return self.username


class EventModel(models.Model):
    name = models.CharField(max_length=512)
    category = models.ForeignKey("CategoryModel", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:event_detail', kwargs={'pk': self.pk})


class CollectionsModel(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True)
    event = models.ManyToManyField(EventModel, blank=True)
    image = models.ImageField(upload_to='collection_images/', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('users:collection_detail', kwargs={'pk': self.pk})


class CategoryModel(models.Model):
    name = models.CharField(max_length=512)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name
