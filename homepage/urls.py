from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('membership/',views.membership,name='membership'),
    path('projects_activities/',views.projects_activities,name='projects & activities'),
    path('events/',views.events,name='events'),
    path('contact/',views.contact,name='contact'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path("resources/", views.resources, name="resources")


]