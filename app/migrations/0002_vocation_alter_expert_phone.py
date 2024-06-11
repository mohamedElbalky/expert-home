# Generated by Django 4.2 on 2024-06-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=25)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='expert',
            name='phone',
            field=models.CharField(max_length=25),
        ),
    ]
