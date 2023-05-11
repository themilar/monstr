import pytest

from monstr.users.models import User
from monstr.tickets.models import Ticket, Label
from monstr.users.tests.factories import UserFactory
from monstr.tickets.tests.factories import TicketFactory, LabelFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def ticket(db) -> Ticket:
    return TicketFactory()


@pytest.fixture
def label(db) -> Label:
    return LabelFactory()
