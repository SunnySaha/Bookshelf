from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class BookList(models.Model):
    author = models.CharField(max_length=255)
    pdf_file = models.FileField()
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_upload = models.DateTimeField(default=timezone.now)
    make_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('homepage')


