# Generated by Django 5.0.3 on 2024-03-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('image1', models.ImageField(upload_to='pics')),
                ('description1', models.TextField()),
            ],
        ),
    ]
