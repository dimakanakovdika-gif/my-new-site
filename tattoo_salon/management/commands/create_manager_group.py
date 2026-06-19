from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from tattoo_salon.models import Master, Service, Appointment

class Command(BaseCommand):
    help = 'Creates Manager group with permissions to manage salon data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating Manager group...')

        # Get content types for models
        master_ct = ContentType.objects.get_for_model(Master)
        service_ct = ContentType.objects.get_for_model(Service)
        appointment_ct = ContentType.objects.get_for_model(Appointment)

        # Create or get Manager group
        manager_group, created = Group.objects.get_or_create(name='Manager')

        if created:
            self.stdout.write('Manager group created.')
        else:
            self.stdout.write('Manager group already exists, updating permissions.')

        # Clear existing permissions
        manager_group.permissions.clear()

        # Add permissions for all models
        permissions = Permission.objects.filter(
            content_type__in=[master_ct, service_ct, appointment_ct]
        )

        manager_group.permissions.add(*permissions)

        self.stdout.write('Manager group has been set up with permissions to manage masters, services, and appointments.')