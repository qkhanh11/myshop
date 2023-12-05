from django.shortcuts import render
from .models import HeroModel
from about.models import *

# Create your views here.
def home(request):
    hero = []
    hero = HeroModel.objects.all()
    OurTeam = OurteamModel.objects.all()[:4]
    about = AboutModel.objects.first()
    context = {
        'hero': hero,
        'ourTeam': OurTeam,
        'about': about
    }
    return render(request,"home/home.html",context)
