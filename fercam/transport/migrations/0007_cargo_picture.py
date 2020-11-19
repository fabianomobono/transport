# Generated by Django 3.1.1 on 2020-10-17 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0006_auto_20201009_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo_picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo_picture', models.ImageField(blank=True, upload_to='cargo_images')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_picture', to='transport.order')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_pictures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]