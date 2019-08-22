from django.shortcuts import render
from django.http import HttpResponse
from info.models import Activities
from django.contrib.auth.models import User
# Create your views here.
posts = [
    {
        'author': 'Corey MS',
        'title': 'First Post',
        'date_posted': '27 August, 2019',
        'content': 'First Post was Published'
    },
    {
        'author': 'Davis MS',
        'title': 'Second Post',
        'date_posted': '28 August, 2019',
        'content': 'Second Post was Published'
    }
]


def Home(request):
    print(request.user)
    context = {
    'Activities': Activities.objects.filter(user_name=request.user)
    }

    return render(request, 'info/home.html', context)

def About(request):
    return render(request, 'info/about.html',{ 'title': 'About Us'})
