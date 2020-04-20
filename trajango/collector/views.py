from django.http import HttpResponse
from .models import Device, Location
from datetime import datetime
from django.utils.timezone import make_aware


def index(request):
    try:
        dev_id = int(request.GET.get('id', ''))
        lat = request.GET.get('lat', '')
        lon = request.GET.get('lon', '')
        timestamp = int(request.GET.get('timestamp', ''))
        created_datetime = make_aware(datetime.fromtimestamp(timestamp))
        accuracy = float(request.GET.get('accuracy', ''))
        batt = float(request.GET.get('batt', ''))
        bearing = float(request.GET.get('bearing', ''))
        altitude = float(request.GET.get('altitude', ''))
        speed = float(request.GET.get('speed', ''))

    except KeyError as e:
        print(e)
        return HttpResponse(e)
    except ValueError as e:
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
                                accuracy=accuracy,
                                batt=batt,
                                bearing=bearing,
                                speed=speed,
                                timestamp=created_datetime)
        return HttpResponse("OK")
    return HttpResponse("You're at the collector index.")
