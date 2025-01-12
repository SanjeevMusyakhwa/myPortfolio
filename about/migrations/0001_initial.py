# Generated by Django 5.1.4 on 2025-01-12 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('happy_clients', models.BigIntegerField(default=0)),
                ('experience_year', models.BigIntegerField(default=0)),
                ('projects_completed', models.BigIntegerField(default=0)),
                ('image', models.ImageField(upload_to='about/', verbose_name='About Image')),
            ],
        ),
    ]
