# Generated by Django 3.1.3 on 2022-01-09 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20220109_0927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='data',
            new_name='date',
        ),
    ]
