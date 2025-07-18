from django.db import models

# Create your models here.


class UsersOrder(models.Model):
    Order_id = models.CharField(max_length=100, unique=True)
    Order_name = models.CharField(max_length=100)
    User_id = models.CharField(max_length=100, unique=True)
    Placed_at = models.DateTimeField(null=True)
