from django.db import models

# Create your models here.

class eMath(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    class Meta:
        db_table = 'MathApp_E_Math'