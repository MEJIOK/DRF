from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from materials.models import Subscription


@shared_task
def send_email_task(course_id):
    """Отправка сообщения пользователю."""

    subscriptions = Subscription.objects.filter(course=course_id)
    for subscription in subscriptions:
        course = subscription.course
        user = subscription.user
        send_mail(
            "Новое обновление",
            "Ваши материалы курса обновились".format(course.title),
            EMAIL_HOST_USER,
            [user.email]
        )
        print(f"Письмо отправлено пользователю {user.email}")
