from django.contrib import admin
from .models import SalesPerson, Leads
# Register your models here.

admin.site.register(Leads)
admin.site.register(SalesPerson)