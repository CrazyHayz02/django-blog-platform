from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Post  # import your model

@receiver(post_save, sender=User)
def make_user_staff_and_grant_perms(sender, instance, created, **kwargs):
    if created:  # Only run for newly created users
        # Make them staff
        instance.is_staff = True
        instance.save(update_fields=['is_staff'])

        # Grant view_post permission
        view_perm = Permission.objects.get(codename='view_post')
        instance.user_permissions.add(view_perm)