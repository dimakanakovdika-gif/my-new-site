from django.apps import AppConfig

class TattooSalonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tattoo_salon'
    
    def ready(self):
        import tattoo_salon.signals