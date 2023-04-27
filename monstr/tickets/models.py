from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from django.conf import settings


class Ticket(TimeStampedModel):
    # category priority and status + as choices or related models

    subject = models.CharField("Subject of the ticket", max_length=255)
    content = models.TextField("Content", blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.subject

    # def get_absolute_url(self):
    #     return reverse("ticket:detail",kwargs={"slug":self.name})


class Label(models.Model):
    class Category(models.TextChoices):
        TYPE = "type", "Type"
        STATUS = "status", "Status"
        PRIORITY = "priority", "Priority"

    class Colour(models.TextChoices):
        RED = "r", "Red"
        GREEN = "gn", "Green"
        BLUE = "b", "Blue"
        YELLOW = "y", "Yellow"
        GREY = "gy", "Grey"
        PURPLE = "p", "Purple"

    category = models.CharField(
        "Category of the label", max_length=10, choices=Category.choices
    )
    name = models.CharField(
        "Name of the label", max_length=20, default="unspecified", unique=True
    )
    colour = models.CharField(
        "Associated colour", max_length=10, choices=Colour.choices, default=Colour.GREY
    )
    ticket = models.ForeignKey(
        Ticket, null=True, on_delete=models.SET_NULL, related_name="labels"
    )

    def __str__(self):
        return f"{self.category.title()}: {self.name.title()}"