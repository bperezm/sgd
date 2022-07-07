from django.contrib import admin
from .models import Proyect, Spring, Developer, SpringConfiguration, Activity


@admin.register(Proyect)
class ProyectAdmin(admin.ModelAdmin):
    list_display = ['name', 'acronym', 'start_date', 'end_date', 'status']



@admin.register(Spring)
class SpringAdmin(admin.ModelAdmin):
    list_display = ['proyect', 'name', 'start_date', 'end_date', 'total_hours']


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'language']


@admin.register(SpringConfiguration)
class SpringConfigurationAdmin(admin.ModelAdmin):
    list_display = ['spring', 'developer', 'working_hours']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'ut', 'type', 'project_phase', 'start_date', 'end_date']
