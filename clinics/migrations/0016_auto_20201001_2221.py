# Generated by Django 3.1.1 on 2020-10-01 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0015_auto_20201001_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinic',
            old_name='Email',
            new_name='email',
        ),
    ]