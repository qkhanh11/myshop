from django.shortcuts import render
from .models import *

# Create your views here.
def about(request):
    video = VideoModel.objects.order_by("-update_at").first()
    about = []
    about = AboutModel.objects.filter(delete_flag=False)
    OurTeam = OurteamModel.objects.all()
    context = {
        "video": video,
        "about": about,
        "ourTeam": OurTeam
    }
    return render(request,"about/about.html",context)
