from django.db import models


class URL(models.Model):
    """
    Model of URL table.
    """

    original_path = models.URLField(unique=True)
    shortcut = models.URLField(unique=True)
