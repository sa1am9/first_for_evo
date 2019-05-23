from django.shortcuts import render
from uploader.models import Upload
from uploader.forms import UploadForm
from django.http import HttpResponseRedirect
from django.urls import reverse
#from celery.task import periodic_task

#@periodic_task(run_every=crontab(hour="*", minute="0", day_of_week="*"), ignore_result=True)
def home(request):
    if request.method == "POST":
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        img = UploadForm()

    images = Upload.objects.all().order_by('-expired_date')

    return render(request, 'home.html', {'form': img, 'images': images})
