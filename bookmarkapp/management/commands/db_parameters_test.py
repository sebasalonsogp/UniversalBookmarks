from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = "Testing the database connection parameters"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully connected to the database\n'))
        self.stdout.write(self.style.SUCCESS(f'Database engine: {connection.settings_dict["ENGINE"]}\n'))
        self.stdout.write(self.style.SUCCESS(f'Database name: {connection.settings_dict["NAME"]}\n'))
        self.stdout.write(self.style.SUCCESS(f'Database user: {connection.settings_dict["USER"]}\n'))
        self.stdout.write(self.style.SUCCESS(f'Database host: {connection.settings_dict["HOST"]}\n'))
        self.stdout.write(self.style.SUCCESS(f'Database port: {connection.settings_dict["PORT"]}\n'))