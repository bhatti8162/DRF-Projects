from rest_framework.viewsets import ModelViewSet
from .models import College, Student
from .serializers import CollegeSerializer, StudentSerializer

class CollegeViewSet(ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
