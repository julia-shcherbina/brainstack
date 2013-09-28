from django import forms

from core.models import UserProfile, Project, Participation
from core.choices import ROLE


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=255, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Project name'}))
    username = forms.CharField(max_length=255, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))

    def create_user(username):
        password = UserProfile.objects.make_random_password(length=10)
        user = UserProfile.objects.create_user(username=username,
            password=password)
        return user

    def create_project(project_title, user):
        project = Project.objects.create(title=project_title)
        project.participants.add(user)
        project.save()
        return project

    def create_participant(user, project):
        participant = Participation.objects.create(user=user, project=project,
            role=ROLE.OWNER)
        return participant

    def save(self):
        username = self.cleaned_data['username']
        project_title = self.cleaned_data['title']
        user = self.create_user(username)
        project = self.create_project(project_title, user)
        self.create_participant(user, project)
        return (project, user)

