# Generated by Django 4.1.7 on 2023-03-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfwnetzwerk', '0004_remove_kostentraeger_ansprechpartner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='vorschlaege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorschlag', models.CharField(max_length=50, verbose_name='Vorschlag')),
                ('begruendung', models.TextField(verbose_name='Begründung')),
                ('vorschlagdatum', models.DateField(auto_now_add=True, verbose_name='vorgeschlagen am')),
                ('bearbeitet', models.DateTimeField(verbose_name='bearbeitet am')),
                ('kommentar', models.CharField(max_length=250, verbose_name='Kommentar')),
                ('erledigt', models.BooleanField(default=False, verbose_name='Erledigt')),
            ],
            options={
                'verbose_name': 'Vorschlag',
                'verbose_name_plural': 'Vorschläge',
            },
        ),
        migrations.AlterField(
            model_name='reha',
            name='dauer',
            field=models.CharField(max_length=50, verbose_name='Dauer'),
        ),
        migrations.AlterField(
            model_name='schlagwort',
            name='schlagwort',
            field=models.CharField(max_length=250, unique=True, verbose_name='Schlagwort'),
        ),
    ]