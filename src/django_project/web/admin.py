from django.contrib import admin
from django.contrib.admin import ListFilter

# import models
from web.models import (
    Event,
    PresentationRequest,
    Resource,
    ResourceCategory,
    TopicSuggestion,
)


class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display: list[str] = ["id", "created_at", "updated_at", "name"]
    search_fields: list[str] = ["id", "name"]
    list_filter: list[str | type[ListFilter] | tuple[str, type[ListFilter]]] = []


class ResourceAdmin(admin.ModelAdmin):
    list_display: list[str] = ["id", "created_at", "updated_at", "name", "description", "url", "category"]
    search_fields: list[str] = ["id", "name", "description", "url"]
    list_filter: list[str] = ["category"]


class TopicSuggestionAdmin(admin.ModelAdmin):
    list_display: list[str] = ["id", "created_at", "updated_at", "title", "description", "skill_level", "email"]
    search_fields: list[str] = ["id", "title", "description", "skill_level", "email"]
    list_filter: list[str] = ["skill_level"]


class PresentationRequestAdmin(admin.ModelAdmin):
    list_display: list[str] = [
        "id",
        "created_at",
        "updated_at",
        "presenter",
        "email",
        "title",
        "description",
        "target_audience",
    ]
    search_fields: list[str] = ["id", "presenter", "email", "title", "description", "target_audience"]
    list_filter: list[str] = ["target_audience"]


class EventAdmin(admin.ModelAdmin):
    list_display: list[str] = [
        "id",
        "created_at",
        "updated_at",
        "name",
        "start_date_time",
        "end_date_time",
        "location",
        "description",
    ]
    search_fields: list[str] = ["id", "name", "location", "description"]
    list_filter: list[str | type[ListFilter] | tuple[str, type[ListFilter]]] = []


# register models
admin.site.register(ResourceCategory, ResourceCategoryAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(TopicSuggestion, TopicSuggestionAdmin)
admin.site.register(PresentationRequest, PresentationRequestAdmin)
admin.site.register(Event, EventAdmin)
