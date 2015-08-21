from django.contrib import admin
from .models import *
from django.contrib.admin import SimpleListFilter

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    pass


class EventPlaceAdmin(admin.ModelAdmin):
    pass


class TicketAdmin(admin.ModelAdmin):
    search_fields = ['event__name']
    fieldsets = (
        (None, {
            'fields': ('event', 'type', 'price', 'place')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('sector', 'row')
        }),
    )
    show_full_result_count = True
    list_filter = ('price', 'event')


admin.site.register(Event, EventAdmin)
admin.site.register(EventPlace, EventPlaceAdmin)
admin.site.register(Ticket, TicketAdmin)
