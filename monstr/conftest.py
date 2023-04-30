import pytest

from monstr.users.models import User
from monstr.tickets.models import Ticket
from monstr.users.tests.factories import UserFactory
from monstr.tickets.tests.factories import TicketFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def ticket(db) -> Ticket:
    return TicketFactory()
