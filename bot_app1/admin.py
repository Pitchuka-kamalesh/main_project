from django.contrib import admin
from .models import Treatment_Model, PerformanceModel

# todo: admin site register
# Register your models here.
admin.site.register(Treatment_Model)

admin.site.register(PerformanceModel)
