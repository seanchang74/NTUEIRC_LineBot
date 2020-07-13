from django.db import models

class users(models.Model):
    uid = models.CharField(max_length=50, null=False)
    question = models.CharField(max_length=250, null=False)
    
    def __str__(self):
        return self.uid
class registerform(models.Model):
    cid = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=15, blank=True, default='')
    email = models.EmailField(max_length=30, blank=True, default='')
    fbname = models.CharField(max_length=30, blank=True, default='')
    lineid = models.CharField(max_length=30, blank=True, default='')
    willing = models.CharField(max_length=5, null=False)
    firsttime = models.CharField(max_length=5, null=False)
    
    def __str__(self):
        return self.cid
