from factory import Faker, SubFactory, fuzzy
from factory.django import DjangoModelFactory
from monstr.tickets.models import Ticket, Label
from monstr.users.tests.factories import UserFactory


class TicketFactory(DjangoModelFactory):
    subject = Faker("sentence", nb_words=4)
    content = Faker(
        "sentence",
        nb_words=8,
    )
    creator = SubFactory(UserFactory)

    class Meta:
        model = Ticket
        # django_get_or_create = ["subject",]


class LabelFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=8)
    colour = fuzzy.FuzzyChoice([x[0] for x in Label.Colour.choices])

    category = fuzzy.FuzzyText(length=8)

    class Meta:
        model = Label
