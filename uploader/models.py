from django.db import models
import os
import datetime


class Upload(models.Model):
    pic = models.FileField(upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField()
