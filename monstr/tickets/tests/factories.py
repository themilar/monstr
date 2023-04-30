from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from monstr.tickets.models import Ticket
from monstr.users.tests.factories import UserFactory

class TicketFactory(DjangoModelFactory):
    subject = Faker("sentence",nb_words=4)
    content = Faker("sentence",nb_words=8)
    creator = SubFactory(UserFactory)
    class Meta:
        model = Ticket
        # django_get_or_create = ["subject",]

