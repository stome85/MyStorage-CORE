# Generated by Django 4.1 on 2022-09-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_path',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
