# Generated by Django 5.1.4 on 2025-01-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_category_protfolio_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protfolio',
            name='category',
        ),
        migrations.AlterField(
            model_name='protfolio',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
