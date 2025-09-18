from django.contrib import admin
from . models import Leadership
from . models import Projects
from . models import Event
from . models import Resource

# Register your models here.

@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('leader_name', 'leader_position', 'leader_caption')
    search_fields = ('leader_name', 'leader_position')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'created_at')
    search_fields = ('title',)


@admin.register(Event)
    list_display = ("title", "start_date", "end_date", "location", "created_at")
    list_filter = ("start_date", "end_date")
    search_fields = ("title", "description", "location")
    ordering = ("start_date",)



@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'status')   # Columns to show in admin list view
    list_filter = ('status',)                       # Sidebar filters
    search_fields = ('name', 'description')         # Search bar for resources
    ordering = ('name',)                             #arrange alphabetically
