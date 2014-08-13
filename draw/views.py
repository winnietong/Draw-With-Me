from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from forms import EmailUserCreationForm, UserForm
from models import *


def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def profile(request):

    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/profile/")
    else:
        form = UserForm(instance=request.user)
    return render(request, "profile.html", {'form': form})


def profile_username(request, profile_username):
    profile_user = User.objects.get(username=profile_username)
    return render(request, "profile_username.html", {'profile_user': profile_user})
