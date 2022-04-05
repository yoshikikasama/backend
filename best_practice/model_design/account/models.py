from django.db import models


class User(models.Model):
    name = models.CharField('name', max_length=20)
    # address = models.CharField('address', max_length=256)


class Address(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='addr')
    address = models.CharField('address', max_length=256)