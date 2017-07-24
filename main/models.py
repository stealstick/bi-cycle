from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from account.models import User
class Cloth(models.Model):
    cloth_name = models.CharField(max_length=40)
    size = models.CharField(max_length=20, null=True, default="L")
    category = models.CharField(max_length=20, null=True)
    bo_prize = models.CharField(max_length=20, null=True)
    lent_prize = models.CharField(max_length=20, null=True)
    cloth_img = models.ImageField(upload_to='cloth_image', default="cloth_image/default.png")
    cloth_intro = models.TextField()
    cloth_about = models.TextField(null=True)
    owner = models.ForeignKey(User, related_name='owner_clother', null=True)
    lenter = models.ForeignKey(User, related_name='lenter_clother', null=True)
    def __str__(self):
        return '%s' % self.cloth_name
