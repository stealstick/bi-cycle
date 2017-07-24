from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from account.models import User
from main.models import Cloth
class Send(models.Model):
    text = models.TextField(null=True)
    cloth= models.ForeignKey(Cloth, related_name='clother_name', null=True)
    owner = models.ForeignKey(User, related_name='owner_lother', null=True)
    resiver = models.ForeignKey(User, related_name='lenter_lother', null=True)
    update_date = models.DateTimeField()
    def __str__(self):
        return '%s' % self.resiver
