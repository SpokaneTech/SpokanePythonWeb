from django.contrib.sitemaps import Sitemap


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages."""

    priority = 1.0
    changefreq = "daily"

    def items(self) -> list[str]:
        return ["/"]

    def location(self, item: str) -> str:
        return item


sitemaps = {
    "static": StaticViewSitemap,
}
