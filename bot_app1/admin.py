from django.contrib import admin
from .models import Treatment_Model,PerformanceModel


# Register your models here.
admin.site.register(Treatment_Model)

admin.site.register(PerformanceModel)