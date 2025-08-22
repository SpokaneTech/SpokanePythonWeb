"""filtersets for applicable app models"""

from rest_framework_filters.filters import BooleanFilter, RelatedFilter
from rest_framework_filters.filterset import FilterSet

# import models
from web.models import (
    Event,
    PresentationRequest,
    Resource,
    ResourceCategory,
    TopicSuggestion,
)


class EventFilterSet(FilterSet):
    """filterset class for Event"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Event
        fields = {
            "created_at": "__all__",
            "description": "__all__",
            "end_date_time": "__all__",
            "id": "__all__",
            "location": "__all__",
            "name": "__all__",
            "start_date_time": "__all__",
            "updated_at": "__all__",
            "url": "__all__",
        }


class PresentationRequestFilterSet(FilterSet):
    """filterset class for PresentationRequest"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = PresentationRequest
        fields = {
            "created_at": "__all__",
            "description": "__all__",
            "email": "__all__",
            "id": "__all__",
            "presenter": "__all__",
            "skill_level": "__all__",
            "title": "__all__",
            "updated_at": "__all__",
        }


class ResourceFilterSet(FilterSet):
    """filterset class for Resource"""

    category = RelatedFilter(
        "ResourceCategoryFilterSet", field_name="category", queryset=ResourceCategory.objects.all()
    )

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Resource
        fields = {
            "category": "__all__",
            "created_at": "__all__",
            "description": "__all__",
            "id": "__all__",
            "name": "__all__",
            "updated_at": "__all__",
            "url": "__all__",
        }


class ResourceCategoryFilterSet(FilterSet):
    """filterset class for ResourceCategory"""

    resources = RelatedFilter("ResourceFilterSet", field_name="resources", queryset=Resource.objects.all())
    has_resources = BooleanFilter(field_name="resources", lookup_expr="isnull", exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = ResourceCategory
        fields = {
            "created_at": "__all__",
            "id": "__all__",
            "name": "__all__",
            "updated_at": "__all__",
        }


class TopicSuggestionFilterSet(FilterSet):
    """filterset class for TopicSuggestion"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = TopicSuggestion
        fields = {
            "created_at": "__all__",
            "description": "__all__",
            "email": "__all__",
            "id": "__all__",
            "skill_level": "__all__",
            "title": "__all__",
            "updated_at": "__all__",
        }
