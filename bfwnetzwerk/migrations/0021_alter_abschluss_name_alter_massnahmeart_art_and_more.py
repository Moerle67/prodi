# Generated by Django 4.1.7 on 2023-09-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfwnetzwerk', '0020_abschluss_produkt_abschluss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abschluss',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Abschluss'),
        ),
        migrations.AlterField(
            model_name='massnahmeart',
            name='art',
            field=models.CharField(max_length=250, primary_key=True, serialize=False, verbose_name='Kategorie'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='dauer',
            field=models.CharField(max_length=150, verbose_name='Dauer'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='dokument',
            field=models.URLField(blank=True, null=True, verbose_name='Dokument'),
        ),
        migrations.RemoveField(
            model_name='produkt',
            name='massnahmeart',
        ),
        migrations.AlterField(
            model_name='produkt',
            name='praxisdauer',
            field=models.CharField(blank=True, max_length=150, verbose_name='Praxisdauer'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='massnahmeart',
            field=models.ManyToManyField(to='bfwnetzwerk.massnahmeart', verbose_name='Maßnahmenart'),
        ),
    ]