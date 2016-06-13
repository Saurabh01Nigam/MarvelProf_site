from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    city = models.CharField(max_length = 10,unique =True)
    contact_number = models.CharField(max_length = 10)
    school = models.CharField(max_length = 50)	
    Class = models.CharField(max_length = 10)
    


    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
