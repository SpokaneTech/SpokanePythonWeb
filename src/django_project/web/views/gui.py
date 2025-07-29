from typing import Any

from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView
from handyhelpers.views.htmx import HtmxFormPostSimple, HtmxPartialView
from web.forms import PresentationRequestForm, TopicSuggestionForm
from web.models import Event, Resource, ResourceCategory


class IndexView(TemplateView):
    template_name = "web/full/index.html"


class ResourceListPartialView(View):
    def get(self, request, pk) -> HttpResponse:
        category: Any = ResourceCategory.objects.get_object_or_none(pk=pk)
        if category:
            resources: BaseManager[Resource] = Resource.objects.filter(category=category)
        else:
            resources = Resource.objects.none()
        color_map: dict[int, str] = {
            1: "primary",
            2: "secondary",
            3: "info",
            4: "success",
            5: "warning",
            6: "danger",
        }
        return render(
            request,
            "web/partials/resource_list.htm",
            {
                "category": category,
                "resources": resources,
                "color": color_map.get(pk, "primary"),
            },
        )


class PastEventsPartialView(View):
    def get(self, request) -> HttpResponse:
        events: BaseManager[Event] = Event.objects.filter(start_date_time__lt=timezone.now()).order_by(
            "-start_date_time"
        )
        return render(request, "web/partials/past_events.htm", {"events": events})


class FutureEventsPartialView(View):
    def get(self, request) -> HttpResponse:
        events: BaseManager[Event] = Event.objects.filter(start_date_time__gte=timezone.now()).order_by(
            "start_date_time"
        )
        return render(request, "web/partials/future_events.htm", {"events": events})


class PresentationRequestPartialView(HtmxPartialView):
    htmx_template_name: str = "web/partials/presentation_request.htm"


class TopicSuggestionPartialView(HtmxPartialView):
    htmx_template_name: str = "web/partials/topic_suggestion.htm"


class PresentationRequestFormPostView(HtmxFormPostSimple):
    form = PresentationRequestForm


class TopicSuggestionFormPostView(HtmxFormPostSimple):
    form = TopicSuggestionForm
