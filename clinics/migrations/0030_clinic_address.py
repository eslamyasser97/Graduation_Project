# Generated by Django 3.1.1 on 2020-10-03 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0029_auto_20201003_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='address',
            field=models.CharField(default=1, max_length=30, verbose_name='المحافظه'),
            preserve_default=False,
        ),
    ]
