# Generated by Django 4.1.7 on 2023-02-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfwnetzwerk', '0018_remove_reha_kostentraeger_reha_kostentraeger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reha',
            name='status',
            field=models.BooleanField(verbose_name='aktiv'),
        ),
    ]
