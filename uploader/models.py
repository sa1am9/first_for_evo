from django.forms import ModelForm
from django.db import models


class Upload(models.Model):
    pic = models.FileField(upload_to="images/")
    time = models.DurationField()
    upload_date = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.time
# FileUpload form class.
class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('pic','time')