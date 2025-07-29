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
    path("htmx/past-events/", gui.PastEventsPartialView.as_view(), name="htmx_past_events"),
    path("htmx/future-events/", gui.FutureEventsPartialView.as_view(), name="htmx_future_events"),
    path(
        "htmx/presentation-request/", gui.PresentationRequestPartialView.as_view(), name="partial_presentation_request"
    ),
    path("htmx/topic-suggestion/", gui.TopicSuggestionPartialView.as_view(), name="partial_topic_suggestion"),
    path(
        "htmx/post-presentation-request/",
        gui.PresentationRequestFormPostView.as_view(),
        name="post_presentation_request",
    ),
    path(
        "htmx/post-topic-suggestion/",
        gui.TopicSuggestionFormPostView.as_view(),
        name="post_topic_suggestion",
    ),
]
