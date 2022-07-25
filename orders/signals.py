from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender = User)
def create_group(sender,created, instance,**kwargs):
    if created:
        group = Group.objects.get(name__iexact = "business class")
        group.user_set.add(instance)

