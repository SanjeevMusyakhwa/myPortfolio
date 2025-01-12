# Generated by Django 5.1.4 on 2025-01-12 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Protfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='protfolio/', verbose_name='Protfolio Image')),
                ('link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
