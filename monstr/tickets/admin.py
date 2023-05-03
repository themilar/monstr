from typing import Any
from django.contrib import admin
from .models import Ticket, Label
from .forms import TicketForm

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("subject",)}
    form = TicketForm


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
