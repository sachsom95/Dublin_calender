from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from profiles.models import Calender
from django.views.generic import CreateView
from django.urls import reverse
# Create your views here.


@login_required
def home(request):

    events = Calender.objects.filter(user__username=request.user)
    context = {'events': events
               }
    return render(request, 'calender/home.html', context)


# Testing class based views
# class PostListView(ListView):
#     model = Calender
#     template_name = 'calender/home.html'
#     queryset = Calender.objects.filter(user__username=request.user)
#     context_object_name = 'events'

# CreateView
class EventCreateView(CreateView):
    model = Calender
    fields = ['event', 'start_date', 'end_date', 'description']
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
