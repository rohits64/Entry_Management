from django.conf import settings
from django.db import models
from django.utils import timezone
 
# Create your models here.
from django.urls import reverse
 
class Hosts(models.Model):
    name  = models.CharField('Host Name',max_length=120)
    email = models.CharField('Email',max_length=120)
    phone = models.IntegerField()
    # address = models.CharField('Address',max_length=120)

    def __str__(self):
        return self.name

class Visitors(models.Model):
    name  = models.CharField('Visitor Name',max_length=120)
    email = models.CharField('Email',max_length=120)
    phone = models.IntegerField()
    name_of_host_id= models.ForeignKey(Hosts,on_delete=models.CASCADE)
    check_in = models.DateTimeField(default=timezone.now)
    check_out_v = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def check_out(self):
        self.check_out_v = timezone.now()
        self.save()