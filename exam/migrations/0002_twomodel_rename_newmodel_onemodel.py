# Generated by Django 5.1.5 on 2025-01-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integer', models.IntegerField(max_length=1000)),
                ('date', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='NewModel',
            new_name='OneModel',
        ),
    ]
