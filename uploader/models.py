from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Upload(models.Model):
    pic = models.FileField(upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField()
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def is_overdue(self):
        if datetime.today() > self.expired_date:
            return True
        return False