# Generated by Django 4.1.7 on 2023-05-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfwnetzwerk', '0019_remove_produkt_massnahmeart_produkt_massnahmeart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abschluss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Abschluss')),
                ('bemerkung', models.TextField(verbose_name='Bemerkung')),
            ],
            options={
                'verbose_name': 'Abschluss',
                'verbose_name_plural': 'Abschlüsse',
            },
        ),
        migrations.AddField(
            model_name='produkt',
            name='abschluss',
            field=models.ManyToManyField(to='bfwnetzwerk.abschluss', verbose_name='Abschluß / Zertifikat'),
        ),
    ]