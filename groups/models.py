from django.db import models
from django.utils import timezone


# Create your models here.
class Group(models.Model):
    author = models.ForeignKey('auth.User')
    members = models.ManyToManyField('auth.User',related_name="is_a_member")
    location = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject + self.members
