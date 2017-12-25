from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Site(models.Model):
    site_name=models.CharField(max_length=255)
    latitude=models.DecimalField(max_digits=13,decimal_places=10)
    longitude=models.DecimalField(max_digits=13,decimal_places=10)
    email=models.EmailField(max_length=254)
    threshold=models.DecimalField(max_digits=20,decimal_places=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name
