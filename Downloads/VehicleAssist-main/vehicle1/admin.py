from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(customer)
admin.site.register(mechanic)
admin.site.register(service_Request)
admin.site.register(mech_request)