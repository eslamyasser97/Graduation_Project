# Generated by Django 3.1.1 on 2020-10-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0012_clinic_works_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='works_hour',
            field=models.IntegerField(max_length=10, verbose_name=': ساعات العمل اليوميه'),
        ),
    ]
