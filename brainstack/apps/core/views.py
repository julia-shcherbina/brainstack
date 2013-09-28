from django.views.generic.base import TemplateView


class MainTemplateView(TemplateView):
    template_name = 'index.html'


class SPAView(TemplateView):
    template_name = 'spa.html'
