import uuid

from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=60)
    short_name = models.CharField(max_length=4)
    app = models.ForeignKey('base.App')


def new_uuid():
    return uuid.uuid4().hex

class App(models.Model):
    title = models.CharField(max_length=64)
    uuid = models.CharField(max_length=32, default=new_uuid, editable=False, db_index=True)
    user = models.ForeignKey('auth.User')