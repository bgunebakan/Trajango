from django.http import HttpResponse
from .models import Device, Location


def index(request):
    try:
        dev_id = int(request.GET.get('id', ''))
        lat = request.GET.get('lat', '')
        lon = request.GET.get('lon', '')
        timestamp = request.GET.get('timestamp', '')
        hdop = request.GET.get('hdop', '')
        altitude = request.GET.get('altitude', '')
        speed = request.GET.get('speed', '')

    except KeyError as e:
        print(e)
        return HttpResponse(e)

    try:
        device = Device.objects.get(dev_id=dev_id)
    except Device.DoesNotExist as e:
        print(e)
        return HttpResponse(e)

    if device:
        Location.objects.create(device=device,
                        lat=lat,
                        lon=lon,
                        altitude=altitude,
                        hdop=hdop,
                        speed=speed,
                        timestamp=timestamp)
        return HttpResponse("OK")
    return HttpResponse("You're at the collector index.")
