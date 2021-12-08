from django.contrib import admin
from .models import *

admin.site.site_header = admin.site.site_title = "Digital_Society"
# Register your models here.

admin.site.register(Role)
admin.site.register(Master)
admin.site.register(Society_member)
admin.site.register(Society_secretary)
