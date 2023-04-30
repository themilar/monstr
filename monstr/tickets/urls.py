from django.urls import path, reverse
from .views import TicketDetailView, TicketListView

app_name="tickets"
urlpatterns = [
    path(
        "",
        view=TicketListView.as_view(),
        name="list",
    ),
    path("<str:slug>/", view=TicketDetailView.as_view(), name="detail"),
]
