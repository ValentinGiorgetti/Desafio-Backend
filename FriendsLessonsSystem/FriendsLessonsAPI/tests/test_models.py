from django.test import TestCase
from django.db.utils import IntegrityError
from FriendsLessonsAPI.models import User, Course, Enrollment

class CourseModelTest(TestCase):

    def setUp(self):
        self.math = Course.objects.create(name='Math', description='Math course')

    def test_course_creation(self):
        """Check if the course was successfully created"""

        self.assertEqual(self.math.name, 'Math')
        self.assertEqual(self.math.description, 'Math course')

    def test_unique_name(self):
        """Check if course name cannot be duplicated"""

        other_course = Course(name='Math')
        self.assertRaises(IntegrityError, other_course.save)

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='Joe', last_name='Smith', username='joe123', birth_date='2000-01-01')

    def test_user_creation(self):
        """Check if the user was successfully created"""

        self.assertEqual(self.user.first_name, 'Joe')
        self.assertEqual(self.user.last_name, 'Smith')
        self.assertEqual(self.user.username, 'joe123')
        self.assertEqual(self.user.birth_date, '2000-01-01')

    def test_unique_username(self):
        """Check if username cannot be duplicated"""

        other_user = User(first_name='Mark', last_name='Johnson', username='joe123', birth_date='1999-12-31')
        self.assertRaises(IntegrityError, other_user.save)

class EnrollmentModelTest(TestCase):

    def setUp(self):
        self.math = Course.objects.create(name='Math')
        self.user = User.objects.create(first_name='Joe', last_name='Smith', username='joe123', birth_date='2000-01-01')

    def test_enrollment_creation(self):
        """Check if the enrollment is successfully created"""

        enrollment = Enrollment.objects.create(user=self.user, course=self.math)
        self.assertEqual(enrollment.user, self.user)
        self.assertEqual(enrollment.course, self.math)
        self.assertEqual(enrollment.lessons_taken, 0)

    def test_positive_integer_lessons_taken(self):
        """Check the number of lessons taken cannot be a negative number"""

        enrollment = Enrollment(user=self.user, course=self.math, lessons_taken=-3)
        self.assertRaises(IntegrityError, enrollment.save)

    def test_unique_enrollment(self):
        """Check that a user cannot enroll more than once in the same course"""

        Enrollment.objects.create(user=self.user, course=self.math)
        other_enrollment = Enrollment(user=self.user, course=self.math)
        self.assertRaises(IntegrityError, other_enrollment.save)              