from django.views.generic import TemplateView


class QueryView(TemplateView):
    template_name = "help/query.html"
