from django.shortcuts import render
from django.http import HttpResponse
from . models import Leadership

# Create your views here
def welcome(request):
    return render(request, 'welcome.html')

def aboutus(request):
    leaders = Leadership.objects.all()  # fetch all leaders
    return render(request,'aboutus.html', {'leaders':leaders})

def membership(request):
    return render(request, 'membership.html')

def projects_activities(request):
    return render(request,'projects_activities.html')

def events(request):
    return render(request,'events.html')

def contact(request):
    return render(request,'contact.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')


def resources(request):
    return render(request, "resources.html")
