# Generated by Django 2.2.1 on 2019-06-02 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='salario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
