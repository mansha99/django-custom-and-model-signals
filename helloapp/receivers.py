from django.dispatch import receiver
from helloapp import signals
from .models import Notice
from django.db.models import signals as modelSignals

@receiver(signals.user_visit_signal)
def handle_user_visit(sender, date_time,ip,device, **kwargs):
    message = "Visit to view {sender}, at {date_time} , IP is {ip} , Device is {device}".format(sender=sender,date_time=date_time,ip=ip,device=device) 
    print(message)

@receiver(modelSignals.post_save, sender=Notice) 
def valid_notice_created(sender, instance, created, **kwargs):
    if created:
        message = "Notice Created : id = {id} ".format(id=instance.id) 
        print(message)

@receiver(signals.invalid_notice_signal)
def invalid_notice_created(sender, **kwargs):
    message = "Alert!!! Someone tried to create Invalid notice" 
    print(message)