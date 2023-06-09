from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Ticket, Label


# define save from
class TicketAdminForm(ModelForm):
    labels = ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        widget=CheckboxSelectMultiple,
    )

    def save(self):
        ticket = super(TicketAdminForm, self).save(commit=False)
        ticket.save()
        input_labels = self.cleaned_data["labels"]
        ticket.labels.set(i for i in input_labels)
        return ticket


    class Meta:
        model = Ticket
        fields = ("subject", "content", "slug", "creator")
