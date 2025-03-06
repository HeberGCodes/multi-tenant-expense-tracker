from django.db import models
from tenants.models import Tenant
from django.contrib.auth import get_user_model
from django_tenants.utils import schema_context

User = get_user_model() 
    

class Company(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE) # Every company belongs to a tenant (helps enforce data integrity)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Expenses(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('travel', 'Travel'),
        ('office', 'Office Supplies'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]
    
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        """
        Ensures that objects are always saved in the correct tenant schema.
        """
        if not self.tenant_id:
            raise ValueError("Expenses must have a tenant assigned.")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.user.username} - {self.amount} ({self.category})'


