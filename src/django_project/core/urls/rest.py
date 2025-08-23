from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from web.views import viewsets

app_name = "rest"

router = routers.DefaultRouter()

# web API Endpoints
router.register(r"event", viewsets.EventViewSet, "event")
router.register(r"presentationrequest", viewsets.PresentationRequestViewSet, "presentationrequest")
router.register(r"resource", viewsets.ResourceViewSet, "resource")
router.register(r"resourcecategory", viewsets.ResourceCategoryViewSet, "resourcecategory")
router.register(r"topicsuggestion", viewsets.TopicSuggestionViewSet, "topicsuggestion")


urlpatterns = [
    # API views
    path("", include(router.urls)),
    path("v1/", include(router.urls)),
]
