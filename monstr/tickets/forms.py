from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Ticket, Label


# define save from
class TicketForm(ModelForm):
    labels = ModelMultipleChoiceField(queryset=Label.objects.all(), required=False)

    def save(self, commit=True):
        ticket = super(TicketForm, self).save(commit=False)
        ticket.save()
        input_labels = self.cleaned_data["labels"]
        ticket.labels.set(i for i in input_labels)
        return ticket

    class Meta:
        model = Ticket
        fields = ("subject", "content", "slug", "creator")
