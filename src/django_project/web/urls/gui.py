from django.urls import path
from web.views import gui

urlpatterns = [
    # GUI views
    path("", gui.IndexView.as_view(), name=""),
    path("index/", gui.IndexView.as_view(), name="index"),
    path("default/", gui.IndexView.as_view(), name="default"),
    path("home/", gui.IndexView.as_view(), name="home"),
    # HTMX views
    path("htmx/resource-list/<int:pk>/", gui.ResourceListPartialView.as_view(), name="htmx_resource_list"),
    path("htmx/past-events/", gui.PastEventsView.as_view(), name="htmx_past_events"),
    path("htmx/future-events/", gui.FutureEventsView.as_view(), name="htmx_future_events"),
    path(
        "htmx/presentation-request/", gui.PresentationRequestFormRequestView.as_view(), name="htmx_presentation_request"
    ),
    path("htmx/topic-suggestion/", gui.TopicSuggestionFormRequestView.as_view(), name="htmx_topic_suggestion"),
]
