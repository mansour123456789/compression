from django.db import models
# Create your models here.
import datetime
import os



def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Item(models.Model):
    name = models.TextField(max_length=191)
    name = models.TextField(max_length=191)
    price = models.TextField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    image = models.TextField(max_length=500, null=True)
   


