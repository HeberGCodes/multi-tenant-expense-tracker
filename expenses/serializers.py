from rest_framework import serializers
from .models import Expenses, Company

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'
        read_only_fields = ('tenant', 'company',)
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'is_default', 'created_at']
        read_only_fields = ['id', 'created_at']