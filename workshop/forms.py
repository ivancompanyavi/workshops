from django import forms
from .models import Workshop, Question

CLASS_ATTR = {'class': 'form-control'}

class WorkshopModelForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['name', 'description', 'prerequisites', 'objectives']
        widgets = {
            'name': forms.TextInput(attrs=CLASS_ATTR),
            'description': forms.Textarea(attrs=CLASS_ATTR),
            'prerequisites': forms.Textarea(attrs=CLASS_ATTR),
            'objectives': forms.Textarea(attrs=CLASS_ATTR),
        }


class QuestionModelForm(forms.ModelForm):
    OPTION_CHOICES = ((0, 'Option 1'),
                      (1, 'Option 2'),
                      (2, 'Option 3'),
                      (3, 'Option 4'))
    opt_1 = forms.CharField(label='Option 1', widget=forms.TextInput(attrs=CLASS_ATTR))
    opt_2 = forms.CharField(label='Option 2', widget=forms.TextInput(attrs=CLASS_ATTR))
    opt_3 = forms.CharField(label='Option 3', widget=forms.TextInput(attrs=CLASS_ATTR))
    opt_4 = forms.CharField(label='Option 4', widget=forms.TextInput(attrs=CLASS_ATTR))

    correct_option = forms.ChoiceField(label='Correct option', choices=OPTION_CHOICES, widget=forms.Select(attrs=CLASS_ATTR))

    class Meta:
        model = Question
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs=CLASS_ATTR),
            }


class QuestionAnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        """
        We can receive a list of strings representing the different options the user can select
        """
        if 'options' in kwargs:
            options = kwargs.pop('options')
        else:
            options = ()
        super(QuestionAnswerForm, self).__init__(*args, **kwargs)

        self.fields['answer'] = forms.ChoiceField(label='Answer', choices=options)


class NewCommentForm(forms.Form):
    message = forms.CharField(label="New comment", widget=forms.Textarea(attrs=CLASS_ATTR))