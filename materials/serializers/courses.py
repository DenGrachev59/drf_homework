from rest_framework import serializers
from materials.models import Courses


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'