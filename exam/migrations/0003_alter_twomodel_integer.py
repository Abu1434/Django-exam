# Generated by Django 5.1.5 on 2025-01-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_twomodel_rename_newmodel_onemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twomodel',
            name='integer',
            field=models.IntegerField(),
        ),
    ]
