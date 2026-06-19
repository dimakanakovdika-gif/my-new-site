from django.db import models
from django.contrib.auth.models import User

class Master(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя мастера")
    experience = models.IntegerField(verbose_name="Опыт работы (лет)")
    specialization = models.TextField(verbose_name="Специализация")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    price_from = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена от")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждена'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email", blank=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    date = models.DateField(verbose_name="Дата сеанса")
    time = models.TimeField(verbose_name="Время сеанса")
    message = models.TextField(verbose_name="Дополнительная информация", blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ['-created_at']

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Оценка")
    text = models.TextField(verbose_name="Отзыв")
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер", blank=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.name} - {self.rating} звезд"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название работы")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='portfolio/', verbose_name="Изображение")
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Работа в портфолио"
        verbose_name_plural = "Портфолио"
        ordering = ['-created_at']

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name="Отправитель")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', verbose_name="Получатель")
    text = models.TextField(verbose_name="Текст сообщения")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    
    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.text[:50]}"
    
    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['-created_at']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Аватар")
    bio = models.TextField(blank=True, verbose_name="О себе")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    
    def __str__(self):
        return f"Профиль {self.user.username}"
    
    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"