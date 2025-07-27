from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "web/custom/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Welcome to the Homepage"
        context["events"] = [
            "May 2024: Cloud Computing Panel",
            "April 2024: Python for Beginners Workshop",
            "March 2024: Tech Career Fair",
        ]
        return context
