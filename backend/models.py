from django.db import models

#from django.db import models

class YourModel(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'your_existing_table_name'
