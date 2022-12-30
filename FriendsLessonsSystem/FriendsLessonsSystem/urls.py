"""FriendsLessonsSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from FriendsLessonsAPI import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users-friends-list/', views.UsersFriendsList.as_view(), name='users-friends-list'),
    path('user-friends/<int:pk>/', views.UserFriendsDetail.as_view(), name='user-friends'),
    path('user-lessons-taken/<int:pk>/', views.UserCoursesDetail.as_view(), name='user-lessons-taken'),
    path('courses/', views.CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
]
