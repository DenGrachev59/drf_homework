from rest_framework.viewsets import ModelViewSet

from materials.models import Courses
from materials.serializers.courses import CoursesSerializer


class CoursesViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer