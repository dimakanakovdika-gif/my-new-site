from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Полностью сбрасывает базу данных и заполняет тестовыми данными'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput',
            action='store_true',
            help='Не спрашивать подтверждение',
        )
    
    def handle(self, *args, **options):
        if not options['noinput']:
            confirm = input('⚠️  ВНИМАНИЕ: Это удалит ВСЕ данные из базы. Продолжить? (yes/no): ')
            if confirm.lower() != 'yes':
                self.stdout.write(self.style.WARNING('Операция отменена.'))
                return
        
        self.stdout.write('🗑️  Удаление базы данных...')
        
        # Удаляем файл базы данных SQLite
        if os.path.exists('db.sqlite3'):
            os.remove('db.sqlite3')
            self.stdout.write('✅ Файл базы данных удален')
        
        self.stdout.write('🔄 Применение миграций...')
        call_command('makemigrations')
        call_command('migrate')
        
        self.stdout.write('👤 Создание суперпользователя...')
        call_command('createsuperuser')
        
        self.stdout.write('🌱 Заполнение тестовыми данными...')
        call_command('seed_data')
        
        self.stdout.write(self.style.SUCCESS('✅ База данных успешно сброшена и заполнена!'))