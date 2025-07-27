from django.urls import path
from web.views import gui

urlpatterns = [
    # GUI views
    path("", gui.IndexView.as_view(), name=""),
    path("index", gui.IndexView.as_view(), name="index"),
    path("default", gui.IndexView.as_view(), name="default"),
    path("home", gui.IndexView.as_view(), name="home"),
]
