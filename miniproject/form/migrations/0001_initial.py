# Generated by Django 5.0.1 on 2024-01-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('adress', models.CharField(max_length=15)),
                ('emailid', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
