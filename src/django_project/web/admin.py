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
    list_display: list[str] = ["id", "name", "created_at", "updated_at"]
    search_fields: list[str] = ["id", "name"]
    list_filter: list[str | type[ListFilter] | tuple[str, type[ListFilter]]] = []


class ResourceAdmin(admin.ModelAdmin):
    list_display: list[str] = ["id", "name", "description", "url", "category", "created_at", "updated_at"]
    search_fields: list[str] = ["id", "name", "description", "url"]
    list_filter: list[str] = ["category"]


class TopicSuggestionAdmin(admin.ModelAdmin):
    list_display: list[str] = ["id", "title", "description", "skill_level", "email", "created_at", "updated_at"]
    search_fields: list[str] = ["id", "title", "description", "skill_level", "email"]
    list_filter: list[str] = ["skill_level"]


class PresentationRequestAdmin(admin.ModelAdmin):
    list_display: list[str] = [
        "id",
        "presenter",
        "email",
        "title",
        "description",
        "skill_level",
        "created_at",
        "updated_at",
    ]
    search_fields: list[str] = ["id", "presenter", "email", "title", "description", "skill_level"]
    list_filter: list[str] = ["skill_level"]


class EventAdmin(admin.ModelAdmin):
    list_display: list[str] = [
        "id",
        "name",
        "start_date_time",
        "end_date_time",
        "location",
        "description",
        "created_at",
        "updated_at",
    ]
    search_fields: list[str] = ["id", "name", "location", "description"]
    list_filter: list[str | type[ListFilter] | tuple[str, type[ListFilter]]] = []


# register models
admin.site.register(ResourceCategory, ResourceCategoryAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(TopicSuggestion, TopicSuggestionAdmin)
admin.site.register(PresentationRequest, PresentationRequestAdmin)
admin.site.register(Event, EventAdmin)
