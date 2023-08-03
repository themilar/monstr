from django.urls import path, reverse
from . import views

app_name="tickets"
urlpatterns = [
    path(
        "",
        view=views.TicketListView.as_view(),
        name="list",
    ),
    path("create/",view=views.TicketCreateView.as_view(),name="create"),
    path("<slug:slug>/", view=views.TicketDetailView.as_view(), name="detail"),
    path("labels/<slug:slug>/",view=views.LabelDetailView.as_view(),name="label_detail")
]
