from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollegeViewSet, StudentViewSet

router = DefaultRouter()
router.register('colleges', CollegeViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
