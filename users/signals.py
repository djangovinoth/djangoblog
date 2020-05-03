from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,EdudetailsModel,PermissionModel

# djangovinoth@gmail.com - Sivan@1234567890
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#
# @receiver(post_save, sender=User)
# def create_permissionmodel(sender, instance, created, **kwargs):
#     if created:
#         PermissionModel.objects.create(user=instance)
#
#
#
# @receiver(post_save, sender=User)
# def save_permissionmodel(sender, instance, **kwargs):
#     PermissionModel.objects.create(user=instance)
#     instance.permissionmodel.save()

# @receiver(post_save, sender=User)
# def create_edudetails(sender, instance, created, **kwargs):
#     if created:
#         EdudetailsModel.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_edudetails(sender, instance, **kwargs):
#     instance.edudetailsmodel.save()
