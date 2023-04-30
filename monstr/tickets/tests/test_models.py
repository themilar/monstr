import pytest
from monstr.tickets.models import Ticket


@pytest.mark.django_db
def test_str(ticket: Ticket):
    assert ticket.__str__() == str(ticket)

@pytest.mark.django_db
def test_ticket_slug(ticket: Ticket):
    assert ticket.slug


@pytest.mark.django_db
def test_ticket_get_absolute_url(ticket: Ticket):
    assert ticket.get_absolute_url() == f"/tickets/{ticket.slug}/"
