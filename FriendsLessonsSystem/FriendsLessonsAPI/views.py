from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from FriendsLessonsAPI.serializers import BaseUserSerializer, UserFriends, UserFriends, UserCourses, BaseCourseSerializer
from FriendsLessonsAPI.models import User, Course

class ModelList(APIView):

    def get(self, request):
        list = self.base_class.objects.all()
        serializer = self.base_serializer(list, many=True)
        return Response(serializer.data)

class UserList(ModelList):
    base_class = User
    base_serializer = BaseUserSerializer
    
class UsersFriendsList(ModelList):
    base_class = User
    base_serializer = UserFriends

class CourseList(ModelList):
    base_class = Course
    base_serializer = BaseCourseSerializer

class ModelDetail(APIView):

    def get_object(self, pk):
        try:
            return self.base_class.objects.get(pk=pk)
        except self.base_class.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = self.base_serializer(obj)
        return Response(serializer.data)

class UserFriendsDetail(ModelDetail):
    base_class = User
    base_serializer = UserFriends

class UserCoursesDetail(ModelDetail):
    base_class = User
    base_serializer = UserCourses

class CourseDetail(ModelDetail):
    base_class = Course
    base_serializer = BaseCourseSerializer