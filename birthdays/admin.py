from django.contrib import admin

# Register your models here.
from .models import personal, globos

admin.site.register(personal)
admin.site.register(globos)
