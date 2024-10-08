# Generated by Django 5.1.1 on 2024-09-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('vehicle_type', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('rent_end_at', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_relative_url', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
