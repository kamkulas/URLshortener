from django.db import models


class URL(models.Model):
    full_path = models.URLField()
    shortcut = models.CharField(max_length=255)
