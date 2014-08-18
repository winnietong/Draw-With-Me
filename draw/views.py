import random, string
import re
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from forms import EmailUserCreationForm, UserForm
from models import *


def home(request):
    return render(request, 'index.html')

def random_alphanum_string():
    char_set = string.ascii_letters + string.digits
    result = ""
    for i in range(21):
        result += random.choice(char_set)
    return result

@csrf_exempt
def save_image(request):
    print "Im here"
    if request.method == "POST":
        print "we-re here"
        # print request.method
        # print request.POST
        data = request.POST.copy()
        title = data.get('title')
        image_data = data.get('base64data')
        base64_data = image_data.replace("data:image/png;base64,", "")

        new_file_name = "{}.png".format(random_alphanum_string())
        upload_path_file_name = "draw/static/img/{}".format(new_file_name)
        local_path_file_name = "img/{}".format(new_file_name)

        # print base64_data
        fh = open(upload_path_file_name, "wb")
        fh.write(base64_data.decode('base64'))
        print fh
        d1 = Drawing.objects.create(local_path=upload_path_file_name, title=title)
        d1.save()
        d1.author.add(request.user)
        fh.close()

        return HttpResponse("everything is ok")



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
def profile(request, profile_username):

    profile_user = User.objects.get(username=profile_username)
    drawings = Drawing.objects.filter(author__username=profile_username)
    favorites = Drawing.objects.filter(follower__username=profile_username)
    url = re.sub('/','',request.path)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/'+ profile_username +'/')
    else:
        form = UserForm(instance=request.user)

    return render(request, "profile.html", {'form': form,
                                            'profile_user': profile_user,
                                            'drawings': drawings,
                                            'favorites': favorites,
                                            'url': url
                                            })
