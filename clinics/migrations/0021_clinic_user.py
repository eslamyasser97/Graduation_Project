# Generated by Django 3.1.1 on 2020-10-02 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinics', '0020_auto_20201002_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='user'),
            preserve_default=False,
        ),
    ]
