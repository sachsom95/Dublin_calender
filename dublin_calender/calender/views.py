from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from profiles.models import Calender
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse
# for our class to have same login required ability
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


@login_required
def home(request):

    events = Calender.objects.filter(user__username=request.user)
    context = {'events': events
               }
    return render(request, 'calender/home.html', context)


def share(request, user_name):

    events = Calender.objects.filter(user__username=user_name)
    print(events)
    context = {'events': events,
               'shared': True,
               'username': user_name
               }
    return render(request, 'calender/home.html', context)


# CreateView
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Calender
    fields = ['event', 'start_date', 'end_date', 'description']
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Update view
class EventUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Calender
    fields = ['event', 'start_date', 'end_date', 'description']
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # get post we update
        event = self.get_object()
        if self.request.user == event.user:
            return True
        return False

# delete view


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Calender
    success_url = "/"

    def test_func(self):
        # check if user loggedin
        event = self.get_object()
        if self.request.user == event.user:
            return True
        return False
