# Generated by Django 3.1.1 on 2020-10-02 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0021_clinic_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='user',
        ),
    ]