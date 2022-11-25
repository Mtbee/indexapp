from django.contrib import admin
from .models import ProgressNB, ProgressPB, Registration, Foods, SendRequest, ReceiveRequest

# Register your models here.
admin.site.register(ProgressNB)
admin.site.register(ProgressPB)
admin.site.register(Registration)
admin.site.register(Foods)
admin.site.register(SendRequest)
admin.site.register(ReceiveRequest)