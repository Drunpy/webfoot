from django.contrib import admin
from .models.game import Players, Teams

admin.site.site_header = "Webfoot"
admin.site.site_title = "Webfoot"


@admin.register(Players)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    pass