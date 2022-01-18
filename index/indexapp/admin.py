from django.contrib import admin
from .models import Progress, Registration, Foods, Estimate

# Register your models here.
admin.site.register(Progress)
admin.site.register(Registration)
admin.site.register(Foods)
admin.site.register(Estimate)