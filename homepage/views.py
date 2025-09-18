from django.shortcuts import render
from django.http import HttpResponse
from . models import Leadership
from . models import Projects
from . models import Event, Resource
from django.utils import timezone

# Create your views here
def welcome(request):
    return render(request, 'welcome.html')

def aboutus(request):
    leaders = Leadership.objects.all()  #fetch leaders from the database
    return render(request,'aboutus.html', {'leaders':leaders})

def membership(request):
    return render(request, 'membership.html')

def projects_activities(request):
    projects = Projects.objects.all()
    return render(request,'projects_activities.html', {'projects':Projects})

def events(request):
    now = timezone.now()
    upcoming_events = Event.objects.filter(start_date__gte=now).order_by("start_date")
    past_events = Event.objects.filter(end_date__lt=now).order_by("-start_date")
    
    return render(request, "events.html", {
        "upcoming_events": upcoming_events,
        "past_events": past_events,})

def contact(request):
    return render(request,'contact.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')


def resources(request):
    resources = Resource.objects.all()
    return render(request, "resources.html", {'resources',resources})
