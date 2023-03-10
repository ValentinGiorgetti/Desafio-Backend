import django, os
from django.core.management import call_command
from dotenv import load_dotenv

def init_db():
    """Method to initialize the database with sample data"""

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FriendsLessonsSystem.settings')
    load_dotenv()
    django.setup()

    from FriendsLessonsAPI.models import User, Course, Enrollment

    call_command('flush')
    call_command('makemigrations')
    call_command('migrate')

    joe = User.objects.create(first_name='Joe', last_name='Smith', username='joe123', birth_date='2000-01-01')
    mark = User.objects.create(first_name='Mark', last_name='Johnson', username='mark456', birth_date='1999-12-31')
    jody = User.objects.create(first_name='Jody', last_name='Williams', username='jody789', birth_date='1998-12-30')
    rachel = User.objects.create(first_name='Rachel', last_name='Smith', username='rachel246', birth_date='1997-12-29')
    jane = User.objects.create(first_name='Jane', last_name='Doe', username='jane512', birth_date='1995-05-01')

    joe.friends.add(mark, jody, rachel)
    jane.friends.add(joe, rachel)

    math = Course.objects.create(name='Math', description='Math course')
    spanish = Course.objects.create(name='Spanish', description='Spanish course')
    history = Course.objects.create(name='History', description='History course')

    Enrollment.objects.create(user=rachel, course=math, lessons_taken=3)
    Enrollment.objects.create(user=rachel, course=spanish, lessons_taken=2)

    Enrollment.objects.create(user=jane, course=history, lessons_taken=10)
    Enrollment.objects.create(user=jane, course=math, lessons_taken=1)
    Enrollment.objects.create(user=jane, course=spanish, lessons_taken=5)

    Enrollment.objects.create(user=joe, course=spanish, lessons_taken=1)

if __name__ == '__main__':
    init_db()