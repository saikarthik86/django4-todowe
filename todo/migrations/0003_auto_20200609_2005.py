# Generated by Django 3.0.7 on 2020-06-09 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200608_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='datacompleted',
            new_name='datecompleted',
        ),
    ]
