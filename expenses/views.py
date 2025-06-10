from rest_framework import generics, permissions
from .models import Expenses, Company
from .serializers import ExpenseSerializer, CompanySerializer
from django_filters.rest_framework import DjangoFilterBackend



class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'category': ['exact'],
        'date': ['exact', 'gte', 'lte'],
        'amount': ['exact', 'gte', 'lte'],
    }
    
    def get_queryset(self):
        return Expenses.objects.filter(
            tenant=self.request.tenant, # Only this tenant's expenses
            user=self.request.user # Only this user's expenses
        )

    def perform_create(self, serializer):
        tenant = self.request.tenant
        user = self.request.user
        
        try:
            default_company = Company.objects.get(is_default=True) # Automatically assign the default company
        except Company.DoesNotExist:
            raise Exception("No default company found. Please create one.")
        
        serializer.save(tenant=tenant, user=user, company=default_company)
        
        
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expenses.objects.filter(
            tenant=self.request.tenant # Only this tenant's expenses
            , user=self.request.user # Only this user's expenses
        )
        

class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Company.objects.filter(tenant=self.request.tenant)  # Only this tenant's companies

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.tenant)  # Save the tenant with the company
        

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Company.objects.filter(tenant=self.request.tenant)  # Only this tenant's companies
    
