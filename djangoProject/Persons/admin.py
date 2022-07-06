from django.contrib import admin
from .models import Person

# Register your models here.
admin.site.site_header = "M7MAD OMAR"
admin.site.site_title = "Person"

admin.site.register(Person)

