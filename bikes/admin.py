from django.contrib import admin
from bikes.models import Bike

# Register your models here.
class BikeAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value',)
    search_fields = ('model, brand',)

admin.site.register(Bike, BikeAdmin)