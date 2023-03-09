# Generated by Django 4.1.7 on 2023-03-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'LinguistApp_db_Word',
            },
        ),
    ]