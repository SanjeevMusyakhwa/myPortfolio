# Generated by Django 5.1.4 on 2025-01-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_protfolio_category_alter_protfolio_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protfolio',
            name='short_description',
            field=models.CharField(max_length=195, verbose_name='Short Description'),
        ),
    ]
