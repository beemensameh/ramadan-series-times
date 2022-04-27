from django.contrib import admin

from channels.models import Channel

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'order', 'frequency'
    ]
    list_filter = [
        'frequency'
    ]
