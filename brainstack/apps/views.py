from django.views.generic.base import TemplateView

class HelloView(TemplateView):

    template_name = 'hello.html'
