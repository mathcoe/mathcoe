# Generated by Django 5.0.3 on 2024-03-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='start',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hd1', models.CharField(max_length=250)),
                ('hd2', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('descri1', models.TextField()),
                ('descri2', models.TextField()),
            ],
        ),
    ]
