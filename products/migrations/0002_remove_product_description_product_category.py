# Generated by Django 4.2 on 2023-04-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ПОДУЩКА', 'Подушки'), ('МАТРАС', 'Матрасы')], default='', max_length=255),
        ),
    ]
