from django.http import HttpResponse
from .models import Device, Location
from datetime import datetime
from django.utils.timezone import make_aware
from django.template import loader
from django.contrib.auth.decorators import login_required

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

@login_required
def map(request):
    all_devices = Device.objects.all()
    last_device_locations = list()
    for device in all_devices:
        last_loc = Location.objects.filter(device=device).latest('timestamp')
        last_device_locations.append(last_loc)

    lastest_locations = Location.objects.order_by('-timestamp')[:10]
    template = loader.get_template('map.html')
    context = {
        'lastest_locations': lastest_locations,
        'last_device_locations': last_device_locations,
        'all_devices': all_devices
    }
    return HttpResponse(template.render(context, request))
