from django.contrib import admin

# Register your models here.
from flow.models import pots,plant,GenParams,sprayOn

admin.site.register(pots)
admin.site.register(plant)
admin.site.register(GenParams)
admin.site.register(sprayOn)