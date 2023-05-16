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
        if ticket_id:
            ticket_visits = f"visits{ticket_id}"
        visits = self.request.session.get(ticket_visits, 0)
        self.request.session[ticket_visits] = visits + 1
        context["labels"] = Label.objects.filter(tickets__id=ticket_id)
        context["visits"] = visits

        return context

    # TODO: why didn't kwargs work?


class LabelDetailView(DetailView):
    model = Label

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["labelled_tickets"] = Ticket.objects.filter(
            labels__slug=self.kwargs["slug"]
        )
        return context

    # query performance: 5queries in 7.21seconds ==>~5.93 ~~ now 4queries but in a similar amount of time.
