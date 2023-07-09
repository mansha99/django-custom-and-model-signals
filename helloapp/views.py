from django.http import HttpResponse
from helloapp import signals
from django.utils import formats
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import NoticeSerializer
from django.http import JsonResponse
from rest_framework import status

import datetime
def hello_world(request):
    message = "Hello World"
    date_time = datetime.datetime.now()
    date_time = formats.date_format(date_time, "SHORT_DATETIME_FORMAT")
    ip = get_client_ip(request=request)
    device=request.META['HTTP_USER_AGENT']
    signals.user_visit_signal.send(sender=request ,date_time=date_time,ip=ip,device=device)
    return HttpResponse(message)

@csrf_exempt
@api_view(['POST'])
def createNotice(request):
    serializer = NoticeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(status=status.HTTP_200_OK, data=serializer.data)
    else:
        return JsonResponse(status=status.HTTP_422_UNPROCESSABLE_ENTITY, data=serializer.errors)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip