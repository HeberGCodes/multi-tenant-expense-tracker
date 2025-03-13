from rest_framework import generics, permissions
from .models import Expenses, Company
from .serializers import ExpenseSerializer


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        tenant = self.request.tenant
        user = self.request.user
        
        try:
            default_company = Company.objects.get(is_default=True) # Automatically assign the default company
        except Company.DoesNotExist:
            raise Exception("No default company found. Please create one.")
        
        serializer.save(tenant=tenant, user=user, company=default_company)
        