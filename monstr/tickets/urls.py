from django.urls import path, reverse
from .views import TicketDetailView, TicketListView,LabelDetailView

app_name="tickets"
urlpatterns = [
    path(
        "",
        view=TicketListView.as_view(),
        name="list",
    ),
    path("<slug:slug>/", view=TicketDetailView.as_view(), name="detail"),
    path("labels/<slug:slug>/",view=LabelDetailView.as_view(),name="label_detail")
]
