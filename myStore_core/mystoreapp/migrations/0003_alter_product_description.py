# Generated by Django 4.1 on 2022-09-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0002_remove_product_image_path_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
