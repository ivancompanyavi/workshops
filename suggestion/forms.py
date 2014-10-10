from django import forms
from .models import Suggestion
from .models import Comment


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']