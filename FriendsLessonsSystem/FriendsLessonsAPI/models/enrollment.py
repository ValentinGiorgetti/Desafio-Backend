from django.db import models
from .person import Person
from .course import Course

class Enrollment(models.Model):
    person = models.ForeignKey(Person)
    course = models.ForeignKey(Course)
    times_taken = models.PositiveIntegerField(default=1)