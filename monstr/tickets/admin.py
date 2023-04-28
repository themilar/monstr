from django.contrib import admin
from .models import Ticket, Label


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("subject",)}


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
