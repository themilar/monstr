from django.urls import resolve, reverse

from monstr.tickets.models import Ticket, Label


def test_ticket_list():
    assert reverse("tickets:list") == "/tickets/"

    assert resolve("/tickets/").view_name == "tickets:list"


def test_ticket_detail(ticket: Ticket):
    assert (
        reverse("tickets:detail", kwargs={"slug": ticket.slug})
        == f"/tickets/{ticket.slug}/"
    )

    assert resolve(f"/tickets/{ticket.slug}/").view_name == "tickets:detail"


def test_label_detail(label: Label):
    assert (
        reverse("tickets:label_detail", kwargs={"slug": label.slug})
        == f"/tickets/labels/{label.slug}/"
    )
    assert resolve(f"/tickets/labels/{label.slug}/").view_name == "tickets:label_detail"
