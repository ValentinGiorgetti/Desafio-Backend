from rest_framework import serializers

from FriendsLessonsAPI.models import User, Course, Enrollment

class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['friends']

class UserFriends(serializers.ModelSerializer):

    friends = BaseUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

class BaseCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class BaseEnrollmentSerializer(serializers.ModelSerializer):

    course = BaseCourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        exclude = ['id', 'user']

class UserCourses(BaseUserSerializer):

    courses = serializers.SerializerMethodField()

    def get_courses(self, obj):
        students = obj.enrollment_set.all()
        serializer = BaseEnrollmentSerializer(students, many=True)
        return serializer.data
