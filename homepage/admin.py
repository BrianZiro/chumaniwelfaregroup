from django.contrib import admin
from . models import Leadership
from . models import Projects

# Register your models here.

@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('leader_name', 'leader_position', 'leader_caption')
    search_fields = ('leader_name', 'leader_position')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'created_at')
    search_fields = ('title',)
