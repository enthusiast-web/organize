# Generated by Django 2.2.6 on 2019-10-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191004_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valores',
            name='pagar_em',
            field=models.DateField(),
        ),
    ]