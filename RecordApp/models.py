from django.db import models

# Create your models here.

class eRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    class Meta:
        db_table = 'RecordApp_E_Record'