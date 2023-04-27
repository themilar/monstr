from django.contrib import admin
from .models import Ticket,Label

admin.site.register(Label)
admin.site.register(Ticket)
