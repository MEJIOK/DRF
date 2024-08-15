from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create a superuser.'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = input("Email address: ")
        password = input("Password: ")

        if not email:
            self.stdout.write(self.style.ERROR("Email is required"))
            return

        if not password:
            self.stdout.write(self.style.ERROR("Password is required"))
            return

        user = User.objects.create_superuser(email=email, password=password)
        user.save()

        self.stdout.write(self.style.SUCCESS(f"Superuser created successfully with email: {email}"))
