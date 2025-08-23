from handyhelpers.serializers import FkReadWriteField
from rest_flex_fields import FlexFieldsModelSerializer

# import models
from web.models import (
    Event,
    PresentationRequest,
    Resource,
    ResourceCategory,
    TopicSuggestion,
)


class EventSerializer(FlexFieldsModelSerializer):
    """serializer class for Event"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Event
        fields = [
            "created_at",
            "description",
            "end_date_time",
            "id",
            "location",
            "name",
            "start_date_time",
            "updated_at",
            "url",
        ]


class PresentationRequestSerializer(FlexFieldsModelSerializer):
    """serializer class for PresentationRequest"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = PresentationRequest
        fields = [
            "created_at",
            "description",
            "email",
            "id",
            "presenter",
            "skill_level",
            "title",
            "updated_at",
        ]


class ResourceSerializer(FlexFieldsModelSerializer):
    """serializer class for Resource"""

    category = FkReadWriteField(queryset=ResourceCategory.objects.all())

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Resource
        fields = [
            "category",
            "created_at",
            "description",
            "id",
            "name",
            "updated_at",
            "url",
        ]

        expandable_fields = {
            "category": "web.serializers.ResourceCategorySerializer",
        }


class ResourceCategorySerializer(FlexFieldsModelSerializer):
    """serializer class for ResourceCategory"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = ResourceCategory
        fields = [
            "created_at",
            "id",
            "name",
            "updated_at",
        ]


class TopicSuggestionSerializer(FlexFieldsModelSerializer):
    """serializer class for TopicSuggestion"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = TopicSuggestion
        fields = [
            "created_at",
            "description",
            "email",
            "id",
            "skill_level",
            "title",
            "updated_at",
        ]
