from django.contrib import admin
from .models import Anchor, Edge ,Meal,Medicine,Food_item

admin.site.register(Anchor)

admin.site.register(Edge)
admin.site.register(Meal)
admin.site.register(Medicine)
admin.site.register(Food_item)