from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from uploader.models import Upload
from uploader.forms import UploadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == "POST":
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        img = UploadForm()

    images = Upload.objects.all().order_by('upload_date')

    return render(request, 'home.html', {'form': img, 'images': images})

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect(home)
    else:
        form = UserCreationForm()
    contex = {'form' : form}
    return render(request, 'registration/registration.html', contex)

