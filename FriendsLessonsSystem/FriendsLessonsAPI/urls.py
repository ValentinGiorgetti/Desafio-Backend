from django.urls import path
from FriendsLessonsAPI import views

app_name = 'api'

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users-friends-list/', views.UsersFriendsList.as_view(), name='users-friends-list'),
    path('user-friends/<int:pk>/', views.UserFriendsDetail.as_view(), name='user-friends'),
    path('user-lessons-taken/<int:pk>/', views.UserCoursesDetail.as_view(), name='user-lessons-taken'),
    path('courses/', views.CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('get-current-weather-conditions/', views.get_current_weather_conditions, name='get-current-weather-conditions'),
]