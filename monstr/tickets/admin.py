from typing import Any
from django.contrib import admin
from .models import Ticket, Label
from .forms import TicketAdminForm

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("subject",)}
    form = TicketAdminForm


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
