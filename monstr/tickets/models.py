from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
from model_utils.models import TimeStampedModel


class Ticket(TimeStampedModel):
    #category priority and status + as choices or related models

    subject = models.CharField("Subject of the ticket", max_length=255)
    content = models.TextField("Content", blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE
    )
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.subject

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("tickets:detail", kwargs={"slug": self.slug})


class Label(models.Model):
    class Category(models.TextChoices):
        TYPE = "type", "Type"
        STATUS = "status", "Status"
        PRIORITY = "priority", "Priority"

    class Colour(models.TextChoices):
        RED = "red", "Red"
        GREEN = "green", "Green"
        BLUE = "blue", "Blue"
        YELLOW = "yellow", "Yellow"
        GREY = "grey", "Grey"
        PURPLE = "purple", "Purple"

    category = models.CharField(
        "Category of the label", max_length=10, choices=Category.choices
    )
    name = models.CharField(
        "Name of the label",
        max_length=20,
        unique=True,
        help_text="Enter the name of the label",
    )
    colour = models.CharField(
        "Associated colour", max_length=10, choices=Colour.choices, default=Colour.GREY
    )
    ticket = models.ForeignKey(
        Ticket, null=True, on_delete=models.SET_NULL, related_name="labels"
    )
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.title()}: {self.name.title()}"

    def get_absolute_url(self):
        return reverse("tickets:label_detail", kwargs={"slug": self.slug})
