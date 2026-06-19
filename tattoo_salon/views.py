from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Master, Service, Appointment, Review, Portfolio, Message, UserProfile
from .forms import AppointmentForm, ReviewForm, UserProfileUpdateForm, MessageForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

@login_required
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    appointments = Appointment.objects.all().order_by('-created_at')
    stats = {
        'total': appointments.count(),
        'pending': appointments.filter(status='pending').count(),
        'confirmed': appointments.filter(status='confirmed').count(),
        'completed': appointments.filter(status='completed').count(),
        'cancelled': appointments.filter(status='cancelled').count(),
    }
    
    return render(request, 'dashboard.html', {
        'appointments': appointments,
        'stats': stats,
    })

def home(request):
    masters = Master.objects.all()[:3]
    services = Service.objects.all()[:4]
    return render(request, 'home.html', {
        'masters': masters,
        'services': services,
    })



def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 
                '✅ Ваша запись успешно отправлена!<br>'
                'Мы свяжемся с вами в ближайшее время для подтверждения.'
            )
            return redirect('appointment')
        else:
            messages.error(request, '❌ Пожалуйста, исправьте ошибки в форме.')
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment.html', {'form': form})

def masters(request):
    masters_list = Master.objects.all()
    return render(request, 'masters.html', {'masters': masters_list})

def services(request):
    services_list = Service.objects.all()
    return render(request, 'services.html', {'services': services_list})

def contact(request):
    return render(request, 'contact.html')

def reviews(request):
    reviews_list = Review.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'reviews.html', {'reviews': reviews_list})

def portfolio(request):
    portfolio_list = Portfolio.objects.all().order_by('-created_at')
    return render(request, 'portfolio.html', {'portfolio': portfolio_list})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.is_published = False  # Отзывы публикуются админом
            review.save()
            messages.success(request, 'Спасибо за ваш отзыв! Он будет опубликован после модерации.')
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # Обновляем данные пользователя
            request.user.first_name = form.cleaned_data.get('first_name', '')
            request.user.last_name = form.cleaned_data.get('last_name', '')
            request.user.email = form.cleaned_data.get('email', '')
            request.user.save()
            
            form.save()
            
            # Обработка очистки аватара
            if request.POST.get('clear_avatar'):
                if user_profile.avatar:
                    user_profile.avatar.delete()
                user_profile.avatar = None
                user_profile.save()
            
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance=user_profile)
        form.initial['first_name'] = request.user.first_name
        form.initial['last_name'] = request.user.last_name
        form.initial['email'] = request.user.email
    
    return render(request, 'profile.html', {
        'form': form,
    })

@login_required
def chat(request):
    # Получаем админа (первого пользователя с is_staff=True)
    admin_user = User.objects.filter(is_staff=True).first()
    if not admin_user:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Администратор не найден.'})
        messages.error(request, 'Администратор не найден.')
        return redirect('home')
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = admin_user
            message.save()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': {
                        'text': message.text,
                        'created_at': message.created_at.isoformat(),
                        'sender': message.sender.username
                    }
                })
            
            messages.success(request, 'Сообщение отправлено!')
            return redirect('chat')
    else:
        form = MessageForm()
    
    # Получаем все сообщения между пользователем и админом
    messages_sent = Message.objects.filter(sender=request.user, receiver=admin_user)
    messages_received = Message.objects.filter(sender=admin_user, receiver=request.user)
    all_messages = (messages_sent | messages_received).order_by('created_at')
    
    return render(request, 'chat.html', {
        'form': form,
        'messages': all_messages,
        'admin_user': admin_user,
    })
    # Добавь эту функцию в конец файла



def play_game(request):
    return render(request, 'game.html') # ТЕПЕРЬ ВСЁ ОК

def game_view(request):
    return render(request, 'game.html') # И ТУТ ТОЖЕ
    # Добавьте это в конец файла views.py
def faq_view(request):
    # Если у вас есть модель FAQ, раскомментируйте строку ниже:
    # from .models import FAQ
    # faqs = FAQ.objects.all()
    
    # Временные данные (пока нет модели в базе данных)
    faqs = [
        {
            "question": "Как записаться на сеанс?",
            "answer": "Вы можете нажать кнопку 'Запись' в меню или воспользоваться нашим 3D симулятором."
        },
        {
            "question": "Нужна ли предварительная консультация?",
            "answer": "Да, для больших работ мы рекомендуем бесплатную консультацию с мастером."
        },
        {
            "question": "Есть ли ограничения по возрасту?",
            "answer": "Мы делаем татуировки строго с 18 лет. При себе необходимо иметь паспорт."
        }
    ]
    
    return render(request, 'faq.html', {'faqs': faqs})