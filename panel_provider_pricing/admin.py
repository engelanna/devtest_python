from django.contrib import admin
from .models import PanelProvider, Country, Location, LocationGroup, TargetGroup

# Register your models here.
admin.site.register(PanelProvider)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(LocationGroup)
admin.site.register(TargetGroup)
