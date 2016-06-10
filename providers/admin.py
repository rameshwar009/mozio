from django.contrib import admin
from .models import *

class ProviderAdmin(admin.ModelAdmin):
	model=Provider

class PolygonAdmin(admin.ModelAdmin):
	model=ProviderPolygon

admin.site.register(Provider,ProviderAdmin)
admin.site.register(ProviderPolygon,PolygonAdmin)
# Register your models here.
