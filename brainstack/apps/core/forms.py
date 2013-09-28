from django import forms


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=255, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Project name'}))
    username = forms.CharField(max_length=255, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
