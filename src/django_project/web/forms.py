# import models
from handyhelpers.forms import HtmxModelForm
from web.models import PresentationRequest, TopicSuggestion


class PresentationRequestForm(HtmxModelForm):
    hx_post: str = "/presentation_request"
    hx_target: str = "presentation-request-form"
    submit_button_text: str = "submit"
    success_message: str = """Presentation request received; thanks!<br/><div
    hx-get="htmx/presentation-request/" 
    hx-trigger="click"
    hx-target="#presentation-request" 
    hx-swap="innerHTML" style="cursor: pointer;">reset form</div>"""

    class Meta:
        model = PresentationRequest
        fields: list[str] = ["presenter", "email", "title", "description", "skill_level"]

        labels: dict[str, str] = {
            "presenter": "Presenter Name",
            "email": "Email Address",
            "title": "Presentation Title",
            "description": "Presentation Description",
            "skill_level": "Skill Level",
        }


class TopicSuggestionForm(HtmxModelForm):
    hx_post: str = "/topic_suggestion"
    hx_target: str = "topic-suggestion-form"
    submit_button_text: str = "submit"
    success_message: str = """Topic suggestion received; thanks!<br/><div
    hx-get="htmx/topic-suggestion/" 
    hx-trigger="click"
    hx-target="#topic-suggestion" 
    hx-swap="innerHTML" style="cursor: pointer;">reset form</div>"""

    class Meta:
        model = TopicSuggestion
        fields: list[str] = ["title", "description", "skill_level", "email"]

        labels: dict[str, str] = {
            "title": "Topic Title",
            "description": "Topic Description",
            "skill_level": "Skill Level",
            "email": "Email Address (optional)",
        }
