# Generated by Django 4.1.7 on 2023-09-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfwnetzwerk', '0025_alter_produkt_dokument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='dokument',
            field=models.URLField(blank=True, help_text='---', null=True, verbose_name='Dokument'),
        ),
    ]
