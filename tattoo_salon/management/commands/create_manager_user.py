from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Creates a manager user with staff status and Manager group'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the manager')
        parser.add_argument('email', type=str, help='Email for the manager')
        parser.add_argument('--password', type=str, help='Password for the manager (optional, will prompt if not provided)')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs.get('password')

        if not password:
            from getpass import getpass
            password = getpass('Enter password for manager: ')

        # Create or get user
        user, created = User.objects.get_or_create(
            username=username,
            defaults={'email': email}
        )

        if created:
            user.set_password(password)
            user.is_staff = True
            user.save()
            self.stdout.write(f'Manager user {username} created.')
        else:
            self.stdout.write(f'Manager user {username} already exists, updating...')

        # Add to Manager group
        manager_group = Group.objects.get(name='Manager')
        user.groups.add(manager_group)

        self.stdout.write(f'User {username} added to Manager group.')