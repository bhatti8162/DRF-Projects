from rest_framework import serializers
from .models import College, Student

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
