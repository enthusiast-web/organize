# Generated by Django 2.2.6 on 2019-10-04 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191004_1334'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rendimentos',
            new_name='Valores',
        ),
        migrations.DeleteModel(
            name='Dispesas',
        ),
    ]