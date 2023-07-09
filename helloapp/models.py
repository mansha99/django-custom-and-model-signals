from django.db import models
from helloapp import signals
class Notice(models.Model):
    title = models.CharField(max_length=80,unique=True)
    description = models.CharField(max_length=255,unique=True)
    def save(self, *args, **kwargs):
        if self.title=="Oops":
            signals.invalid_notice_signal.send(sender=None)
            return 
        else:
            super().save(*args, **kwargs)  
      