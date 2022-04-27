from datetime import datetime, timedelta

from django.db.models import Q
from django.http import HttpResponse
from django.template import loader

from series.models import ChannelSerie

def index(request):
    datetime_now = datetime.now()
    hournow = datetime_now - timedelta(hours=1)
    if datetime_now.hour == 0:
        last_min_in_day = datetime(year=hournow.year, month=hournow.month, day=hournow.day, hour=23, minute=59, second=59)
        first_min_in_day = datetime(year=datetime_now.year, month=datetime_now.month, day=datetime_now.day, hour=0, minute=0, second=0)
        series_now = ChannelSerie.objects.filter(Q(time__gte=hournow.time(), time__lte = last_min_in_day.time()) | Q(time__gte=first_min_in_day.time(), time__lte = datetime_now.time()))
    series_now = ChannelSerie.objects.filter(time__gte=hournow.time(), time__lte = datetime_now.time())
    template = loader.get_template('public/index.html')
    context = {
        'series_now': series_now,
    }
    return HttpResponse(template.render(context, request))

