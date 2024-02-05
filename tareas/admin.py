from django.contrib import admin
from .models import Tarea

class AdministradorTareas(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Tarea, AdministradorTareas)
