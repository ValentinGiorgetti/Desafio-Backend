from django.db import models
from .user import User
from .course import Course

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lessons_taken = models.PositiveIntegerField(default=1)