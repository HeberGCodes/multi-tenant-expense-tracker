from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

"""
Moved these models into a shared app to ensure that the Tenant table 
lives in the public schema. This means that every tenant-specific schema 
can reliably reference the Tenant data and can avoid foreign key errors 
when running migrations.
"""

class Tenant(TenantMixin):
    """
    Represents a tenant in the multi-tenant system.
    Each tenant gets its own schema.
    """
    name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=50, unique=True) # Reqquired for Django-Tenants
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True  # Creates schema on creation
    auto_drop_schema = True  # Deletes schema if tenant is deleted

    def __str__(self):
        return self.name
    

class Domain(DomainMixin):
    """
    Represents a domain for each tenant.
    """
    pass
