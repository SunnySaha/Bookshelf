from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BookList(models.Model):
    author = models.CharField(max_length=255)
    file = models.FileField()
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_upload = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
