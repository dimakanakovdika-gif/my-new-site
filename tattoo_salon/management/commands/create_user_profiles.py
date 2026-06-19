from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tattoo_salon.models import UserProfile

class Command(BaseCommand):
    help = 'Создает UserProfile для существующих пользователей'

    def handle(self, *args, **kwargs):
        users_without_profile = User.objects.filter(userprofile__isnull=True)
        for user in users_without_profile:
            UserProfile.objects.create(user=user)
            self.stdout.write(f'Создан профиль для пользователя: {user.username}')
        
        self.stdout.write(f'Создано профилей: {users_without_profile.count()}')