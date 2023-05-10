from django.urls import resolve, reverse

from monstr.tickets.models import Ticket, Label


def test_ticket_list(ticket: Ticket):
    assert reverse("tickets:list") == "/tickets/"

    assert resolve("/tickets/").view_name == "tickets:list"


def test_ticket_detail(ticket: Ticket):
    assert (
        reverse("tickets:detail", kwargs={"slug": ticket.slug})
        == f"/tickets/{ticket.slug}/"
    )

    assert resolve(f"/tickets/{ticket.slug}/").view_name == "tickets:detail"
