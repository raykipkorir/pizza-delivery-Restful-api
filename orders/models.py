from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

User = get_user_model()

class Order(models.Model):

    SIZES = (
        ("S",'small'),
        ("M",'medium'),
        ("L",'large'),
        ("XL",'extra large'),
    )

    ORDER_STATUS = (
        ("PENDING",'pending'),
        ("IN_TRANSIT",'InTransit'),
        ("DELIVERED",'Delivered'),
    )

    user = models.ForeignKey(User, verbose_name = _("user_id"),on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=SIZES, default = SIZES[0][0])
    order_status = models.CharField(max_length=30, choices = ORDER_STATUS, default = ORDER_STATUS[0][0])
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return f"{self.size} pizza by {self.user.username}"


