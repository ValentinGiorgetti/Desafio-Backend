from django.test import TestCase
from django.urls import reverse
from FriendsLessonsAPI.models import User, Course, Enrollment

class BaseTestClass(TestCase):

    def setUp(self):
        # Create some users
        self.john_doe = User.objects.create(first_name='John', last_name='Doe', username='johndoe', birth_date='1990-01-01')
        self.jane_smith = User.objects.create(first_name='Jane', last_name='Smith', username='janesmith', birth_date='1995-05-01')
        self.bob_johnson = User.objects.create(first_name='Bob', last_name='Johnson', username='bobjohnson', birth_date='1985-03-15')
        self.jody_williams = User.objects.create(first_name='Jody', last_name='Williams', username='jodywilliams', birth_date='1998-12-30')
        self.joe_smith = User.objects.create(first_name='Joe', last_name='Smith', username='joesmith', birth_date='2000-01-01')
        self.usernames = {'johndoe', 'janesmith', 'bobjohnson', 'jodywilliams', 'joesmith'}
        self.user_list = [self.john_doe, self.jane_smith, self.bob_johnson, self.jody_williams, self.joe_smith]

        # Add some friends
        self.bob_johnson.friends.add(self.john_doe, self.jane_smith)
        self.jane_smith.friends.add(self.joe_smith)
        self.friends = { 'bobjohnson' : {'johndoe', 'janesmith'}, 'johndoe' : {'bobjohnson'}, 
                         'janesmith' : {'bobjohnson', 'joesmith'}, 'joesmith' : {'janesmith'}, 'jodywilliams' : set() }

        # Create some courses
        self.mathematics = Course.objects.create(name='Mathematics')
        self.english = Course.objects.create(name='English')
        self.history = Course.objects.create(name='History')
        self.courses = { 'Mathematics', 'English', 'History' }
        self.courses_list = [self.mathematics, self.english, self.history]

        # Create some enrollments
        self.john_doe_mathematics = Enrollment.objects.create(user=self.john_doe, course=self.mathematics, lessons_taken=5)
        self.john_doe_history = Enrollment.objects.create(user=self.john_doe, course=self.history, lessons_taken=1)
        self.john_doe_english = Enrollment.objects.create(user=self.john_doe, course=self.english, lessons_taken=3)

        self.jane_smith_mathematics = Enrollment.objects.create(user=self.jane_smith, course=self.mathematics)
        self.jane_smith_english = Enrollment.objects.create(user=self.jane_smith, course=self.english, lessons_taken=4)

        self.bob_johnson_mathematics = Enrollment.objects.create(user=self.bob_johnson, course=self.mathematics, lessons_taken=10)
        self.bob_johnson_history = Enrollment.objects.create(user=self.bob_johnson, course=self.history, lessons_taken=3)
        self.bob_johnson_english = Enrollment.objects.create(user=self.bob_johnson, course=self.english, lessons_taken=7)
        
        self.user_courses = { 'bobjohnson' : { ('Mathematics', 10), ('History', 3),  ('English', 7) }, 
                              'johndoe' :    { ('Mathematics', 5), ('History', 1),  ('English', 3) }, 
                              'janesmith' :  { ('English', 4) }, 'joesmith' : set(), 'jodywilliams' : set() }

class UserViewTest(BaseTestClass):

    def test_user_list(self):
        """Check if all users are returned"""

        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        usernames = { user['username'] for user in data }

        self.assertEqual(self.usernames, usernames)

    def test_all_user_friends(self):
        """Check if all user friends are returned"""

        response = self.client.get(reverse('users-friends-list'))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        friends = { user['username'] : { friend['username'] for friend in user['friends'] } for user in data }

        self.assertEqual(self.friends, friends)

    def test_user_friends(self):
        """Check if all user friends from a specific user are returned"""

        response = self.client.get(reverse('user-friends', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)

        for user in self.user_list:
            response = self.client.get(reverse('user-friends', kwargs={'pk': user.id}))
            self.assertEqual(response.status_code, 200)

            data = response.json()
            friends = { friend['username'] for friend in data['friends'] }

            self.assertEqual(friends, self.friends[user.username])

    def test_lessons_taken_by_user(self):
        """Check if all courses with 1 or more lessons taken from a specific user are returned"""

        response = self.client.get(reverse('user-lessons-taken', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)

        for user in self.user_list:
            response = self.client.get(reverse('user-lessons-taken', kwargs={'pk': user.id}))
            self.assertEqual(response.status_code, 200)

            data = response.json()
            courses = { (course['course']['name'], course['lessons_taken']) for course in data['courses'] }

            self.assertEqual(courses, self.user_courses[user.username])

class CourseViewTest(BaseTestClass):

    def test_course_list(self):
        """Check if all courses are returned"""

        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, 200)
        
        data = response.json()

        courses = { course['name'] for course in data }
        self.assertEqual(courses, self.courses)

    def test_course(self):
        """Check if the specified course is returned"""

        response = self.client.get(reverse('course-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)

        for course in self.courses_list:
            response = self.client.get(reverse('course-detail', kwargs={'pk': course.id}))
            self.assertEqual(response.status_code, 200)

            data = response.json()

            self.assertEqual(data['name'], course.name)