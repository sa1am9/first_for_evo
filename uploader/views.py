from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from uploader.models import Upload
from uploader.forms import UploadForm
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
def home(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            data['borrower'] = request.user
            Upload.objects.create(**data)
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        form = UploadForm()
    images = Upload.objects.filter(borrower=request.user, expired_date__gte=datetime.now()).order_by('upload_date')
    return render(request, 'home.html', {'form': form, 'images': images})

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
    context = {'form' : form}
    return render(request, 'registration/registration.html', context)

