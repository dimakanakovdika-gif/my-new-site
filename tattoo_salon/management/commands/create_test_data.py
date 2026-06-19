from django.core.management.base import BaseCommand
from tattoo_salon.models import Master, Service, Appointment
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Создает тестовые данные для приложения'
    
    def handle(self, *args, **options):
        # Очищаем существующие данные
        Appointment.objects.all().delete()
        Service.objects.all().delete()
        Master.objects.all().delete()
        
        self.stdout.write('Создание мастеров...')
        masters = [
            Master.objects.create(
                name="Алексей Иванов",
                experience=8,
                specialization="Реализм, портреты, черно-белая татуировка"
            ),
            Master.objects.create(
                name="Мария Петрова", 
                experience=5,
                specialization="Акварель, минимализм, цветные татуировки"
            ),
            Master.objects.create(
                name="Дмитрий Смирнов",
                experience=10,
                specialization="Традишнл, олдскул, японский стиль"
            ),
        ]
        
        self.stdout.write('Создание услуг...')
        services = [
            Service.objects.create(
                name="Консультация",
                description="Бесплатная консультация по выбору эскиза",
                price_from=0
            ),
            Service.objects.create(
                name="Минималистичная татуировка",
                description="Небольшая татуировка простого дизайна",
                price_from=3000
            ),
            Service.objects.create(
                name="Татуировка среднего размера",
                description="Татуировка с детализацией и цветом",
                price_from=8000
            ),
            Service.objects.create(
                name="Крупная татуировка",
                description="Рукав, спина, сложный дизайн",
                price_from=25000
            ),
        ]
        
        self.stdout.write('Создание тестовых записей...')
        # Создаем несколько тестовых записей
        names = ["Иван Петров", "Елена Сидорова", "Алексей Козлов", "Мария Иванова", "Сергей Смирнов"]
        phones = ["+79991234567", "+79997654321", "+79998887766", "+79995554433", "+79992221100"]
        
        for i in range(10):
            Appointment.objects.create(
                name=random.choice(names),
                phone=random.choice(phones),
                email=f"client{i}@example.com",
                master=random.choice(masters),
                service=random.choice(services[1:]),  # кроме консультации
                date=date.today() + timedelta(days=random.randint(1, 30)),
                time=f"{random.randint(10, 18)}:00",
                status=random.choice(['pending', 'confirmed', 'completed']),
                message="Тестовая запись, создана автоматически"
            )
        
        self.stdout.write(self.style.SUCCESS('✅ Тестовые данные успешно созданы!'))
        self.stdout.write(f'Создано: {len(masters)} мастеров, {len(services)} услуг, 10 записей')