from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.views.generic import FormView, TemplateView

from core.forms import ProjectForm


class HomeView(FormView):
    form_class = ProjectForm
    template_name = 'index.html'

    def form_valid(self, form):
        project, user = form.save()
        user = authenticate(username=user.username, password=user.temporary_password)
        login(self.request, user)
        self.kwargs['project_id'] = project.id
        return super(HomeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('spa', args=[self.kwargs['project_id']])


class SPAView(TemplateView):
    template_name = 'spa.html'
