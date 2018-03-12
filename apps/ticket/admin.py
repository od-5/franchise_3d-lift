# coding=utf-8
from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'status', 'created')
    list_filter = ['created', 'status']
    search_fields = ['mail', 'phone']
    date_hierarchy = 'created'
    fields = ('name', 'phone', 'email', 'status')

    def has_add_permission(self, request):
        return False


admin.site.register(Ticket, TicketAdmin)
