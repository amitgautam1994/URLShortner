from django.db import models
from datetime import datetime

# Create your models here.


class ShortURL(models.Model):
    original_url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.original_url

    def detail(self):
        return f"Name: {self.original_url}, School: {self.short_url} ..."
