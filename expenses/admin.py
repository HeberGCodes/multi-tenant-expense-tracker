from django.contrib import admin
from .models import Tenant, Domain, Company, Expenses

admin.site.register(Tenant)
admin.site.register(Domain)
admin.site.register(Company)
admin.site.register(Expenses)

