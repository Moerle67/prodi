# Generated by Django 4.1.7 on 2023-02-17 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bfwnetzwerk', '0013_kostentraeger_ansprechpartner'),
    ]

    operations = [
        migrations.AddField(
            model_name='reha',
            name='kostentraeger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bfwnetzwerk.kostentraeger', verbose_name='Geschäftfeld/Kostenträger'),
        ),
    ]
