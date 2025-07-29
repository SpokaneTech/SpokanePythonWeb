from typing import Any

from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView
from handyhelpers.views.htmx import (
    HtmxFormPostSimple,
)
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


class PastEventsView(View):
    def get(self, request) -> HttpResponse:
        events: BaseManager[Event] = Event.objects.filter(start_date_time__lt=timezone.now()).order_by(
            "-start_date_time"
        )
        return render(request, "web/partials/past_events.htm", {"events": events})


class FutureEventsView(View):
    def get(self, request) -> HttpResponse:
        events: BaseManager[Event] = Event.objects.filter(start_date_time__gte=timezone.now()).order_by(
            "start_date_time"
        )
        return render(request, "web/partials/future_events.htm", {"events": events})


class PresentationRequestFormRequestView(HtmxFormPostSimple):
    form = PresentationRequestForm
    success_message: str = "Presentation request received, thanks!"


class TopicSuggestionFormRequestView(HtmxFormPostSimple):
    form = TopicSuggestionForm
    success_message: str = "Topic suggestion received, thanks!"
