# Generated by Django 3.1.1 on 2020-10-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0008_auto_20201017_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo_picture',
            name='cargo_picture',
            field=models.ImageField(blank=True, upload_to='cargo_images'),
        ),
    ]
