from django.contrib import admin
from .models import Master, Service, Appointment, Review, Portfolio, Message, UserProfile

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'specialization')
    search_fields = ('name', 'specialization')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_from')
    search_fields = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'master', 'service', 'date', 'time', 'status', 'created_at')
    list_filter = ('status', 'date', 'master', 'service')
    search_fields = ('name', 'phone', 'email')
    list_editable = ('status',)
    readonly_fields = ('created_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'master', 'is_published', 'created_at')
    list_filter = ('rating', 'is_published', 'master')
    search_fields = ('name', 'text')
    list_editable = ('is_published',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'master', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'text', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('sender__username', 'receiver__username', 'text')
    list_editable = ('is_read',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'avatar')
    search_fields = ('user__username', 'user__email')