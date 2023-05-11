import pytest
from monstr.tickets.models import Ticket, Label


@pytest.mark.django_db
def test_ticket_str(ticket: Ticket):
    assert ticket.__str__() == str(ticket)


@pytest.mark.django_db
def test_ticket_slug(ticket: Ticket):
    assert ticket.slug


@pytest.mark.django_db
def test_ticket_get_absolute_url(ticket: Ticket):
    assert ticket.get_absolute_url() == f"/tickets/{ticket.slug}/"


@pytest.mark.django_db
def test_label_str(label: Label):
    assert label.__str__() == str(label)


@pytest.mark.django_db
def test_label_get_absolute_url(label: Label):
    assert label.get_absolute_url() == f"/tickets/labels/{label.slug}/"
