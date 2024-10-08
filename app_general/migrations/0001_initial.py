# Generated by Django 5.1.1 on 2024-09-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('status', models.CharField(choices=[('unapproved', 'Unapproved'), ('approved', 'Approved'), ('banned', 'Banned')], default='unapproved', max_length=15)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('vehicle_set', models.ManyToManyField(to='app_vehicles.vehicle')),
            ],
        ),
    ]
