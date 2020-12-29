from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from profiles.models import Calender
# Create your views here.


@login_required
def home(request):

    events = Calender.objects.filter(user__username=request.user)
    context = {'events': events
               }
    return render(request, 'calender/home.html', context)
