from APPS.rest_test.models import *
from rest_framework import serializers


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'address', ]


class SClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SClass
        fields = ['id', 'grade', 'school', ]


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'sclass', ]
