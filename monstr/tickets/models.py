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

    category = models.CharField(max_length=8, choices=Category.choices)
    name = models.CharField(
        "Name of the category", max_length=20, default="unspecified",unique=True
    )
    colour = models.CharField("Associated colour", max_length=20, default="grey")
    ticket = models.ForeignKey(
        Ticket, null=True, on_delete=models.SET_NULL, related_name="labels"
    )
