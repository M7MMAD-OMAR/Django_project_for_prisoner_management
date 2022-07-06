from django.contrib import admin
from .models import Convicts
# Register your models here.
admin.site.site_header = "M7MAD OMAR"
admin.site.site_title = "Convicts"

admin.site.register(Convicts)
