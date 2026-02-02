from rest_framework.viewsets import ModelViewSet
from .models import Employee, Department, Attendance
from .serializers import (
    EmployeeSerializer,
    DepartmentSerializer,
    AttendanceSerializer
)

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
