from django.contrib import admin
from .models import Patient,Hospital_manager,Doctor,Nurse,Receptionist,Department_manager

admin.site.register(Patient)
admin.site.register(Hospital_manager)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Receptionist)
admin.site.register(Department_manager)
