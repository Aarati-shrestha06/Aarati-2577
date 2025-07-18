
# from django.db import models

# # Create your models here.


# class Users(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     birth_date = models.DateTimeField(null=True)


# class Products(models.Model):
#     STATUS = [
#         ('P' ,"pending"),
#         ('C',"completed")
#         ('F', "failed")
#     ]
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique = True)
#     description = models.TextField(max_length=1000)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     inventory = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=1, choices=STATUS, default = 'P')

