from django.contrib.auth import login
from django.views.generic import FormView

from core.forms import ProjectForm


class HomeView(FormView):
    form_class = ProjectForm
    template_name = 'index.html'

    def form_valid(self, form):
        project, user = form.save()
        login(self.request, user)
        super(HomeView, self).form_valid(self, form)


class SPAView(TemplateView):
    template_name = 'spa.html'
