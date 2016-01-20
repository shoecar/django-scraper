from __future__ import unicode_literals
from django.db import models
from djangotoolbox.fields import ListField

class Page(models.Model):
    url = models.URLField()
    params = DictField()
    images = ListField()