from django.contrib import admin
from .models import Hospital,Pharmacy,Department,Floor,Room,Reception,Charging_station,Office,Bio_labs,Scan_lab,Building,Kitchen

admin.site.register(Room)
admin.site.register(Floor)
admin.site.register(Hospital)
admin.site.register(Pharmacy)
admin.site.register(Department)
admin.site.register(Reception)
admin.site.register(Charging_station)
admin.site.register(Office)
admin.site.register(Building)
admin.site.register(Bio_labs)
admin.site.register(Scan_lab)
admin.site.register(Kitchen)