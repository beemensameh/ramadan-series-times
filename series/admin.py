from datetime import datetime, timedelta

from django.contrib import admin
from django.db.models import Q

from series.models import ChannelSerie, Serie


class ChannelSerieInline(admin.TabularInline):
    model = ChannelSerie
    extra = 1

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    inlines = [ChannelSerieInline]
    list_display = [
        'name',
    ]

class TimeFilter(admin.SimpleListFilter):
    title = 'Now'
    parameter_name = 'now'

    def lookups(self, request, model_admin):
        return (
            ("now", "Now"),
        )

    def queryset(self, request, queryset):
        if self.value() == 'now':
            datetime_now = datetime.now()
            hournow = datetime_now - timedelta(hours=1)
            if datetime_now.hour == 0:
                last_min_in_day = datetime(year=hournow.year, month=hournow.month, day=hournow.day, hour=23, minute=59, second=59)
                first_min_in_day = datetime(year=datetime_now.year, month=datetime_now.month, day=datetime_now.day, hour=0, minute=0, second=0)
                return queryset.filter(Q(time__gte=hournow.time(), time__lte = last_min_in_day.time()) | Q(time__gte=first_min_in_day.time(), time__lte = datetime_now.time()))
            return queryset.filter(
                time__gte=hournow.time(), time__lte = datetime.now().time())


@admin.register(ChannelSerie)
class ChannelSerieAdmin(admin.ModelAdmin):
    list_display = [
        'channel', 'channel_order', 'serie', 'time',
    ]

    list_filter = [
        TimeFilter,
    ]


