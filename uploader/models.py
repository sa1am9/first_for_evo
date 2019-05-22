from django.db import models

import datetime
class Upload(models.Model):
    pic = models.FileField(upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField()

    def cheack_date(self):
        date =self.cleane_date['expired_date']
        if datetime.datetime.now()>=date:
            pass