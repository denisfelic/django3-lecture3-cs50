from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime
# Create your views here.


def index(request):
    now = datetime.datetime.now()
    current_date_text = f"{now.year}-{now.month}-{(now.day - 1)}"

    date = datetime.datetime.strptime(
        f"{current_date_text} 00:00:00", "%Y-%m-%d %H:%M:%S")
    current_day = date.timetuple().tm_yday

    time_to_christmas = 365 - current_day
    minutes_to_christmas = (365 - current_day) * 1440 - \
        (now.hour * 60 + now.minute)

    return render(request, 'natal/index.html', {
        'is_christmas': is_natal(now.day - 1, now.month),
        'time_to_christmas': time_to_christmas,
        'minutes_to_christmas': minutes_to_christmas,
    })


def natal_api(request):
    now = datetime.datetime.now()
    current_date_text = f"{now.year}-{now.month}-{(now.day - 1)}"

    date = datetime.datetime.strptime(
        f"{current_date_text} 00:00:00", "%Y-%m-%d %H:%M:%S")
    current_day = date.timetuple().tm_yday

    time_to_christmas = 365 - current_day
    minutes_to_christmas = (365 - current_day) * 1440 - \
        (now.hour * 60 + now.minute)

    return HttpResponse(JsonResponse({
        'is_christmas': is_natal(now.day - 1, now.month),
        'time_to_christmas': time_to_christmas,
        'minutes_to_christmas': minutes_to_christmas,
    }))


def is_natal(day, month):
    if(day == 25 and month == 12):
        return True
    else:
        return False
