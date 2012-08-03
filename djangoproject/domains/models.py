from django.db import models



class DomainName(models.Model):
    name = models.CharField(max_length=256)
    creation_date = models.DateTimeField()
    last_updated = models.DateTimeField()
    expiration_date = models.DateTimeField()
    registrar = models.CharField(max_length=128)