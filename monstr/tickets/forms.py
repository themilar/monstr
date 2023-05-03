from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Ticket, Label


# define save from
class TicketForm(ModelForm):
    labels = ModelMultipleChoiceField(queryset=Label.objects.all(), required=False)

    # def get_initial_for_field(self, field: Field, field_name: str) -> Any:
    #     initial= super().get_initial_for_field(field, field_name)
    #     labels = self.label_set.all()
    def save(self, commit=True):
        ticket = super(TicketForm, self).save(commit=False)
        input_labels = self.cleaned_data['labels']
        # print(self.fields['labels'])
        ticket.labels.set([i for i in input_labels])
        return ticket

    class Meta:
        model = Ticket
        fields = ("subject", "content", "slug", "creator")
