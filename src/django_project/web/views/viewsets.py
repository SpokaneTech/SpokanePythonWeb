"""DRF viewsets for applicable app models"""

from rest_flex_fields import is_expanded
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# import filtersets
from web.filtersets import (
    EventFilterSet,
    PresentationRequestFilterSet,
    ResourceCategoryFilterSet,
    ResourceFilterSet,
    TopicSuggestionFilterSet,
)

# import models
from web.models import (
    Event,
    PresentationRequest,
    Resource,
    ResourceCategory,
    TopicSuggestion,
)

# import serializers
from web.serializers import (
    EventSerializer,
    PresentationRequestSerializer,
    ResourceCategorySerializer,
    ResourceSerializer,
    TopicSuggestionSerializer,
)


class EventViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Events to be viewed"""

    model = Event
    queryset = model.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilterSet


class PresentationRequestViewSet(viewsets.ModelViewSet):
    """API endpoint that allows PresentationRequests to be viewed"""

    model = PresentationRequest
    queryset = model.objects.all()
    serializer_class = PresentationRequestSerializer
    filterset_class = PresentationRequestFilterSet


class ResourceViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Resources to be viewed"""

    model = Resource
    serializer_class = ResourceSerializer
    filterset_class = ResourceFilterSet

    def get_queryset(self):
        queryset = self.model.objects.all().select_related(
            "category",
        )

        if is_expanded(self.request, "category"):
            queryset = queryset.select_related("category")

        return queryset


class ResourceCategoryViewSet(viewsets.ModelViewSet):
    """API endpoint that allows ResourceCategorys to be viewed"""

    model = ResourceCategory
    queryset = model.objects.all()
    serializer_class = ResourceCategorySerializer
    filterset_class = ResourceCategoryFilterSet

    @action(detail=True, methods=["get"])
    def resources(self, request, *args, **kwargs):
        """get the resourcess associated with this ResourceCategory instance if available"""
        instance = self.get_object()
        data = instance.resources.all()
        if data:
            try:
                serializer = ResourceSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("No resources available for this resourcecategory ", status.HTTP_404_NOT_FOUND)


class TopicSuggestionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows TopicSuggestions to be viewed"""

    model = TopicSuggestion
    queryset = model.objects.all()
    serializer_class = TopicSuggestionSerializer
    filterset_class = TopicSuggestionFilterSet
