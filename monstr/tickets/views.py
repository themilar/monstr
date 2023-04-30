from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ticket, Label


class TicketListView(ListView):
    model = Ticket
    context_object_name="tickets"


class TicketDetailView(DetailView):
    model = Ticket
