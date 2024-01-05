from django.core.management.base import BaseCommand
from django.db import connection
from bookmarkapp.models import MyModel  # Replace 'myapp' and 'MyModel' with your actual app and model

class Command(BaseCommand):
    help = "Testing the database connection"

    def handle(self, *args, **options):
        try:
            # Perform a simple database operation to test the connection
            result = MyModel.objects.first()  # Replace with an actual model in your app
            self.stdout.write(self.style.SUCCESS('Successfully connected to the database\n'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error connecting to the database: {str(e)}\n'))
