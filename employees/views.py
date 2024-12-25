# views.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse

from .models import Employee
from .serializers import EmployeeSerializer

# Trang chủ, render template HTML

def home(request):
    return render(request, 'employees/home.html')

# API chính cho Employee với viewsets của Django REST framework
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# API dùng JSONResponse cho danh sách nhân viên
@api_view(['GET'])
@permission_classes([AllowAny])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def employee_table(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

# Custom JWT views
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

class MyTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)
