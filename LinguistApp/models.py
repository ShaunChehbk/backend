from django.db import models

# Create your models here.

class Word(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=32)
    class Meta:
        db_table = "LinguistApp_db_Word"

class RateHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.IntegerField()
    rate = models.SmallIntegerField()
    class Meta:
        db_table = "LinguistApp_db_RateHistory"