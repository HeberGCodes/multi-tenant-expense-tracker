from django.shortcuts import render
from django.http import JsonResponse

def first_api(request):
    data = {
        'message': 'Welcome to my first Expense Tracker API'
    }
    return JsonResponse(data)

