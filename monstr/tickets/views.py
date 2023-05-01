from typing import Any, Dict, Optional
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ticket, Label


class TicketListView(ListView):
    model = Ticket
    context_object_name = "tickets"


class TicketDetailView(DetailView):
    model = Ticket
    context_object_name = "ticket"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        ticket_id = self.get_object().id
        context["labels"] = Label.objects.filter(ticket_id=ticket_id)
        return context

    # TODO: why didn't kwargs work?


class LabelDetailView(DetailView):
    model = Label

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        slug = self.get_object().slug
        context["labelled_tickets"] = Ticket.objects.filter(labels__slug=slug)
        return context
