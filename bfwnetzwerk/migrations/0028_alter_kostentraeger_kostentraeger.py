# Generated by Django 4.1.7 on 2023-10-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfwnetzwerk', '0027_alter_produkt_dokument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kostentraeger',
            name='kostentraeger',
            field=models.CharField(max_length=250, verbose_name='Kostenträger'),
        ),
    ]
