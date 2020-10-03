from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('city', related_name='user_city', on_delete=models.CASCADE,blank=True,null=True)
    telephone = models.CharField(_('رقم الهاتف'),max_length=40)
    image = models.ImageField(_(': الصوره البطاقه الشخصيه'),upload_to='profile',blank=True,null=True)


    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


class city(models.Model):
    name = models.CharField(_('المدينه'),max_length=30)