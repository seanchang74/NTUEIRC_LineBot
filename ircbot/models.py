from django.db import models

class users(models.Model):
    uid = models.CharField(max_length=50, null=False)
    created_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.uid