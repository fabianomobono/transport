# Generated by Django 3.1.1 on 2020-10-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_order_was_placed',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
