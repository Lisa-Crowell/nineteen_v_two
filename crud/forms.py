from django import forms
from .models import IdeaModel


class IdeaForm(forms.ModelForm):
    class Meta:
        model = IdeaModel
        fields = ['idea_title',
                  'idea_description',
                  'idea_author']
