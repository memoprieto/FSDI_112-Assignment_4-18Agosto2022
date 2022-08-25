from django.views.generic import TemplateView

from bs4 import BeautifulSoup
import requests


URL = "https://wttr.in"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 "
        "Safari/537.36 Edg/104.0.1293.63"
        )
}


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        resp = requests.get(URL, headers=HEADERS)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            weather_pre = soup.find("pre")
        else:
            weather_pre = "%s" % resp.text
        context["weather"] = str(weather_pre)
        return self.render_to_response(context)
