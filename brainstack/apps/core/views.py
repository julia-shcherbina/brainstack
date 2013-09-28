from django.views.generic import FormView
from django.core.urlresolvers import reverse

from core.forms import ProjectForm
from core.models import UserProfile, Project, Participant
from core.choices import ROLE


class HomeView(FormView):
    form_class = ProjectForm
    template_name = 'index.html'


class SPAView(TemplateView):
    template_name = 'spa.html'
