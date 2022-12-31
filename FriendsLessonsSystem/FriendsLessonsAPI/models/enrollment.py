from django.db import models
from FriendsLessonsAPI.models import User, Course

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lessons_taken = models.PositiveIntegerField(default=1)