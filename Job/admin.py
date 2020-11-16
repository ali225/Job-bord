from django.contrib import admin

# Register your models here.
from .models import Job, category, Apply

admin.site.register(Job)
admin.site.register(category)
admin.site.register(Apply)
