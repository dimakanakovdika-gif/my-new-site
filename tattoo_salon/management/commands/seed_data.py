from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, time
from tattoo_salon.models import (
    Master, TattooStyle, PortfolioItem, Service, 
    Appointment
)

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаем заполнение базы данных...')
        # Добавляем создание отзывов в функцию handle:

def handle(self, *args, **kwargs):
    # ... существующий код ...
    
    # Создаем отзывы
    self.stdout.write('Создание отзывов...')
    reviews_data = [
        {
            'name': 'Анна',
            'rating': 5,
            'text': 'Делала первую татуировку у Алексея. Очень переживала, но мастер успокоил и профессионально все объяснил. Работа выполнена аккуратно, точно по эскизу. Спасибо!',
            'master': masters[0],
            'is_published': True,
        },
        {
            'name': 'Сергей',
            'rating': 5,
            'text': 'Мария сделала потрясающую акварельную татуировку. Цвета очень яркие, переходы плавные. Оборудование современное, все стерильно. Обязательно вернусь!',
            'master': masters[1],
            'is_published': True,
        },
        {
            'name': 'Ольга',
            'rating': 5,
            'text': 'Делала японский рукав у Дмитрия. Работа заняла несколько сеансов, но результат превзошел все ожидания! Настоящий профессионал своего дела. Рекомендую!',
            'master': masters[2],
            'is_published': True,
        },
        {
            'name': 'Михаил',
            'rating': 4,
            'text': 'Хороший салон, профессиональные мастера. Делал геометрическую татуировку, все ровно и симметрично. Цены адекватные за такое качество.',
            'master': masters[0],
            'is_published': True,
        },
        {
            'name': 'Екатерина',
            'rating': 5,
            'text': 'Искала мастера для перекрытия старой татуировки. Алексей сделал невозможное — полностью перекрыл старую работу, теперь даже не верится, что там что-то было. Мастер с золотыми руками!',
            'master': masters[0],
            'is_published': True,
        },
    ]
    
    for data in reviews_data:
        review = Review.objects.create(**data)
        self.stdout.write(f'Создан отзыв от: {review.name}')
    
    # ... остальной код ...
        # Очищаем существующие данные (осторожно!)
        self.stdout.write('Очистка существующих данных...')
        Appointment.objects.all().delete()
        PortfolioItem.objects.all().delete()
        Service.objects.all().delete()
        TattooStyle.objects.all().delete()
        Master.objects.all().delete()
        
        # Создаем мастеров
        self.stdout.write('Создание мастеров...')
        masters_data = [
            {
                'name': 'Алексей Иванов',
                'experience': 8,
                'specialization': 'Реализм, портреты, черно-белая татуировка',
                'instagram': 'https://instagram.com/alex_tattoo'
            },
            {
                'name': 'Мария Петрова',
                'experience': 5,
                'specialization': 'Акварель, минимализм, цветные татуировки',
                'instagram': 'https://instagram.com/maria_tattoo'
            },
            {
                'name': 'Дмитрий Смирнов',
                'experience': 10,
                'specialization': 'Традишнл, олдскул, японский стиль',
                'instagram': 'https://instagram.com/dmitry_tattoo'
            },
        ]
        
        masters = []
        for data in masters_data:
            master = Master.objects.create(**data)
            masters.append(master)
            self.stdout.write(f'Создан мастер: {master.name}')
        

        
        # Создаем стили тату
        self.stdout.write('Создание стилей тату...')
        styles_data = [
            {'name': 'Реализм', 'description': 'Фотореалистичные изображения'},
            {'name': 'Акварель', 'description': 'Имитация акварельной живописи'},
            {'name': 'Минимализм', 'description': 'Простые и лаконичные рисунки'},
            {'name': 'Олдскул', 'description': 'Классический американский стиль'},
            {'name': 'Традишнл', 'description': 'Традиционный стиль'},
            {'name': 'Японский', 'description': 'Иредзуми, традиционная японская татуировка'},
            {'name': 'Геометрия', 'description': 'Геометрические узоры и орнаменты'},
            {'name': 'Лайнворк', 'description': 'Работы, выполненные линиями'},
        ]
        
        styles = []
        for data in styles_data:
            style = TattooStyle.objects.create(**data)
            styles.append(style)
            self.stdout.write(f'Создан стиль: {style.name}')
        
        # Создаем услуги
        self.stdout.write('Создание услуг...')
        services_data = [
            {
                'name': 'Консультация',
                'description': 'Бесплатная консультация по выбору эскиза и места нанесения',
                'price_from': 0,
                'duration': '30-60 минут'
            },
            {
                'name': 'Минималистичная татуировка',
                'description': 'Небольшая татуировка простого дизайна',
                'price_from': 3000,
                'duration': '1-2 часа'
            },
            {
                'name': 'Татуировка среднего размера',
                'description': 'Татуировка с детализацией и цветом',
                'price_from': 8000,
                'duration': '3-5 часов'
            },
            {
                'name': 'Крупная татуировка (рукав, спина)',
                'description': 'Масштабная работа, выполняется за несколько сеансов',
                'price_from': 25000,
                'duration': '20+ часов'
            },
            {
                'name': 'Перекрытие старой татуировки',
                'description': 'Исправление или перекрытие старой работы',
                'price_from': 10000,
                'duration': 'Зависит от сложности'
            },
            {
                'name': 'Коррекция',
                'description': 'Исправление и доработка существующей татуировки',
                'price_from': 5000,
                'duration': '1-3 часа'
            },
        ]
        
        services = []
        for data in services_data:
            service = Service.objects.create(**data)
            services.append(service)
            self.stdout.write(f'Создана услуга: {service.name}')
        
        # Создаем несколько работ в портфолио
        self.stdout.write('Создание работ в портфолио...')
        portfolio_data = [
            {
                'title': 'Волк в лесу',
                'master': masters[0],
                'style': styles[0],
                'description': 'Реалистичное изображение волка в лесной чаще',
            },
            {
                'title': 'Акварельная роза',
                'master': masters[1],
                'style': styles[1],
                'description': 'Нежная роза в акварельной технике',
            },
            {
                'title': 'Японский дракон',
                'master': masters[2],
                'style': styles[5],
                'description': 'Традиционный японский дракон на плече',
            },
            {
                'title': 'Геометрический узор',
                'master': masters[0],
                'style': styles[6],
                'description': 'Сложный геометрический узор на предплечье',
            },
            {
                'title': 'Минималистичный кот',
                'master': masters[1],
                'style': styles[2],
                'description': 'Простой и лаконичный силуэт кота',
            },
            {
                'title': 'Олдскул якорь',
                'master': masters[2],
                'style': styles[3],
                'description': 'Классический морской мотив в стиле олдскул',
            },
        ]
        
        for data in portfolio_data:
            portfolio_item = PortfolioItem.objects.create(**data)
            self.stdout.write(f'Создана работа: {portfolio_item.title}')
        
        # Создаем тестовые записи
        self.stdout.write('Создание тестовых записей...')
        appointments_data = [
            {
                'name': 'Иван Сидоров',
                'phone': '+79991234567',
                'email': 'ivan@example.com',
                'master': masters[0],
                'service': services[1],
                'date': date.today(),
                'time': time(14, 0),
                'message': 'Хочу сделать тату волка на плече'
            },
            {
                'name': 'Елена Козлова',
                'phone': '+79997654321',
                'email': 'elena@example.com',
                'master': masters[1],
                'service': services[2],
                'date': date.today(),
                'time': time(16, 30),
                'message': 'Интересует акварельная татуировка цветка'
            },
        ]
        
        
        for data in appointments_data:
            appointment = Appointment.objects.create(**data)
            self.stdout.write(f'Создана запись: {appointment.name} - {appointment.date}')
        
        self.stdout.write(self.style.SUCCESS('\n✅ База данных успешно заполнена тестовыми данными!'))
        self.stdout.write('\nСоздано:')
        self.stdout.write(f'  • Мастеров: {len(masters)}')
        self.stdout.write(f'  • Стилей: {len(styles)}')
        self.stdout.write(f'  • Услуг: {len(services)}')
        self.stdout.write(f'  • Работ в портфолио: {PortfolioItem.objects.count()}')
        self.stdout.write(f'  • Записей: {Appointment.objects.count()}')
        