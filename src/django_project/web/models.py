from django.db import models
from django.urls import reverse
from handyhelpers.models import HandyHelperBaseModel


class ResourceCategory(HandyHelperBaseModel):
    """A category for resources."""

    name: models.CharField = models.CharField(max_length=64, unique=True, null=False)

    class Meta:
        ordering: list[str] = ["name"]

    def __str__(self) -> str:
        return self.name


class Resource(HandyHelperBaseModel):
    """A resource for the Spokane Python User Group."""

    name: models.CharField = models.CharField(max_length=128, null=False)
    description: models.TextField = models.TextField(null=True, blank=True)
    url: models.URLField = models.URLField(max_length=200, null=False)
    category: ResourceCategory = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE, related_name="resources")

    class Meta:
        ordering: list[str] = ["created_at"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("web:resource_detail", kwargs={"pk": self.pk})


class TopicSuggestion(HandyHelperBaseModel):
    """A topic suggestion for the Spokane Python User Group."""

    title: models.CharField = models.CharField(max_length=128, null=False)
    description: models.TextField = models.TextField()
    skill_level: models.CharField = models.CharField(
        max_length=32,
        choices=[
            ("all", "All Levels"),
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advanced", "Advanced"),
        ],
        default="all",
    )
    email: models.EmailField = models.EmailField(max_length=254, null=True, blank=True)

    class Meta:
        ordering: list[str] = ["title"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("web:topic_suggestion_detail", kwargs={"pk": self.pk})


class PresentationRequest(HandyHelperBaseModel):
    """A request for a presentation at the Spokane Python User Group."""

    presenter: models.CharField = models.CharField(max_length=64, null=False)
    email: models.EmailField = models.EmailField(max_length=254, null=False)
    title: models.CharField = models.CharField(max_length=128, null=False)
    description: models.TextField = models.TextField()
    target_audience: models.CharField = models.CharField(
        max_length=64,
        null=False,
        choices=[
            ("all", "All Levels"),
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advanced", "Advanced"),
        ],
        default="all",
        help_text="Who is the target audience for this presentation?",
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("web:presentation_detail", kwargs={"pk": self.pk})


class Event(HandyHelperBaseModel):
    """An event for the Spokane Python User Group."""

    name: models.CharField = models.CharField(max_length=128, null=False)
    start_date_time: models.DateTimeField = models.DateTimeField(null=False)
    end_date_time: models.DateTimeField = models.DateTimeField(null=False)
    location: models.CharField = models.CharField(max_length=256, null=True, blank=True)
    description: models.TextField = models.TextField(null=True, blank=True)

    class Meta:
        ordering: list[str] = ["-start_date_time"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("web:event_detail", kwargs={"pk": self.pk})
