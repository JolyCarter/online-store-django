# Generated by Django 4.2 on 2023-05-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
