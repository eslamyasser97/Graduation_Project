# Generated by Django 3.1.1 on 2020-10-01 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0017_auto_20201001_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='password',
            field=models.CharField(default=1, max_length=50, verbose_name=': كلمه المرور'),
            preserve_default=False,
        ),
    ]
