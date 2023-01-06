from FriendsLessonsSystem.celery import app
from django.core.mail import send_mail
from django.conf import settings

@app.task(name="send_notification_email")
def send_notification_email():
    subject = "Ejemplo email - Valentin Giorgetti"
    message = "Un email que se envía cada cierto tiempo"
    from_email = settings.EMAIL_FROM
    recipient_list = [settings.EMAIL_TO]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
    print(f"Email sent from {from_email} to {recipient_list[0]}")