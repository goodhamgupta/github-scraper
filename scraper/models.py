from django.db import models

# Create your models here.


class Authorization(models.Model):

    username = models.CharField(max_length=50,unique=True,blank=False,null=False)
    password = models.TextField(blank=False,null=False)
    email = models.TextField(blank=False,null=False)
    ph_no = models.IntegerField(max_length=12,blank=False,null=False)


    def __unicode__(self):
        return u'{0}|{1}'.format(self.username, self.password)