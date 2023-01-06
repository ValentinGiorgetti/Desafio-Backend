from django.urls import path
from FriendsLessonsAPI import views

app_name = 'api'

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users-friends-list/', views.UsersFriendsListView.as_view(), name='users-friends-list'),
    path('user-friends/<int:pk>/', views.UserFriendsDetailView.as_view(), name='user-friends'),
    path('user-lessons-taken/<int:pk>/', views.UserCoursesDetailView.as_view(), name='user-lessons-taken'),
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('get-current-weather-conditions/', views.CurrentWeatherConditionsView.as_view(), name='get-current-weather-conditions'),
]