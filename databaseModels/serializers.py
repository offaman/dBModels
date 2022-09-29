from rest_framework import serializers
from databaseModels.models import StudentapiStudentinfo

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentapiStudentinfo
        fields = ('studentname','studentrollno','studentbranch','studentgpa','studentsection')
