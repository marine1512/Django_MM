# Generated by Django 5.1.4 on 2025-01-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=150)),
                ('disponible', models.CharField(max_length=150)),
            ],
        ),
    ]
