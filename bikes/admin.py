from django.contrib import admin
from bikes.models import Bike,Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BikeAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value',)
    search_fields = ('model, brand',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Bike, BikeAdmin)
