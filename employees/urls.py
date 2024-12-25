# employees/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, employee_list, MyTokenObtainPairView, MyTokenRefreshView, employee_table

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),                     # Định tuyến cho viewset
    path('employees/', employee_list, name='employee-list'),  # Định tuyến cho view employee_list
    path('employee-table/', employee_table, name='employee-table'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Định tuyến lấy JWT
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'), # Định tuyến làm mới JWT
]
