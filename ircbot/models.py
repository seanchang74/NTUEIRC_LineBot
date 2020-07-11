from django.db import models

class users(models.Model):
    uid = models.CharField(max_length=50, null=False)
    question = models.CharField(max_length=250, null=False)
    
    def __str__(self):
        return self.uid
class registerform(models.Model):
    cid = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=30, null=False)
    fbname = models.CharField(max_length=30, null=False)
    lineid = models.CharField(max_length=30, null=False)
    willing = models.CharField(max_length=5, null=False)
    firsttime = models.CharField(max_length=5, null=False)
    
    def __str__(self):
        return self.id
