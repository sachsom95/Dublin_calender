"""dublin_calender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as calender_views
from django.urls import reverse

# class based view
# path('', calender_views.PostListView.as_view(), name='home'),

urlpatterns = [
    path('', calender_views.home, name='home'),
    path('event/new/', calender_views.EventCreateView.as_view(),
         name='event-create'),
    path('event/<int:pk>/update/', calender_views.EventUpdateView.as_view(),
         name='event-update'),
    path('event/<int:pk>/delete/', calender_views.EventDeleteView.as_view(),
         name='event-delete'),
    path('<str:user_name>/', calender_views.share, name='share'),

]
