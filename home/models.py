# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Riskgroup(models.Model):

    #__Riskgroup_FIELDS__
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    moono = models.CharField(max_length=255, null=True, blank=True)
    addressno = models.CharField(max_length=255, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)

    #__Riskgroup_FIELDS__END

    class Meta:
        verbose_name        = _("Riskgroup")
        verbose_name_plural = _("Riskgroup")



#__MODELS__END
