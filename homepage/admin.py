from django.contrib import admin
from . models import Leadership

# Register your models here.

@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('leader_name', 'leader_position', 'leader_caption')
    search_fields = ('leader_name', 'leader_position')
