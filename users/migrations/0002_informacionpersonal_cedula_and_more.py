# Generated by Django 4.2 on 2023-04-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacionpersonal',
            name='cedula',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='informacionpersonal',
            name='direcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='informacionpersonal',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='fecha de cumpleaño'),
        ),
        migrations.AlterField(
            model_name='informacionpersonal',
            name='estado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='informacionpersonal',
            name='pais',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='informacionpersonal',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='estado civil'),
        ),
        migrations.AlterField(
            model_name='informacionpersonal',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='informacionpersonal',
            name='webside',
            field=models.URLField(blank=True, null=True, verbose_name='redes sociales'),
        ),
    ]
