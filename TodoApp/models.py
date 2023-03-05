from django.db import models

# Create your models here.

class eTodo(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    class Meta:
        db_table = 'TodoApp_E_Record'