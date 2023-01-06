from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from FriendsLessonsAPI.serializers import BaseUserSerializer, UserFriendsSerializer, UserFriendsSerializer, UserCoursesSerializer, BaseCourseSerializer
from FriendsLessonsAPI.models import User, Course

from django.conf import settings
import requests

class UserListView(ListAPIView):
    """View to get a list with all users"""

    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    
class UsersFriendsListView(ListAPIView):
    """View to get a list with all users and their friends"""

    queryset = User.objects.all()
    serializer_class = UserFriendsSerializer

class CourseListView(ListAPIView):
    """View to get a list with all courses"""

    queryset = Course.objects.all()
    serializer_class = BaseCourseSerializer

class UserFriendsDetailView(RetrieveAPIView):
    """View to get a specific user by ID and the user friend list"""

    queryset = User.objects.all()
    serializer_class = UserFriendsSerializer

class UserCoursesDetailView(RetrieveAPIView):
    """View to get a specific user by ID and the courses which the user has taken one or more lessons"""

    queryset = User.objects.all()
    serializer_class = UserCoursesSerializer

class CourseDetailView(RetrieveAPIView):
    """View to get a course by ID"""

    queryset = Course.objects.all()
    serializer_class = BaseCourseSerializer

class CurrentWeatherConditionsView(APIView):
    """View to get current weather conditions using a external API"""

    def get(self, request):
        url = f"{settings.ACCUWEATHER_API_BASE_URL}/{settings.ACCUWEATHER_LOCATION_KEY}?apikey={settings.ACCUWEATHER_API_KEY}"
        response = requests.get(url=url)
        
        data = response.json()
        if response.status_code == 200:
            data = data[0]
            for i in ['EpochTime', 'WeatherIcon', 'IsDayTime', 'MobileLink', 'Link']:
                del data[i]

        return Response(data, status=response.status_code)