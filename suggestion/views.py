from .models import Worker, Suggestion
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from .forms import SuggestionForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def suggestion_list(request):
    suggestions = Suggestion.objects.all()
    suggestion_form = SuggestionForm()
    comment_form = CommentForm()
    data = {'suggestions': suggestions, 'suggestion_form': suggestion_form, 'comment_form': comment_form}
    return render_to_response('suggestions.html', data, RequestContext(request))


@require_POST
def suggestion_add(request):
    form = SuggestionForm(request.POST)
    if form.is_valid():
        worker = Worker.objects.get(user__pk=request.user.pk)
        message = form.cleaned_data['message']
        sug = Suggestion.objects.create(suggester=worker, message=message)
        sug.save()
        return redirect('suggestion_list')


def suggestion_delete(request, suggestion_id):
    try:
        suggestion = Suggestion.objects.get(pk=suggestion_id)
        suggestion.delete()
    except ObjectDoesNotExist:
        messages.add_message(request, messages.INFO,
                             'The suggestion ID "%s" doesn\'t exist' % suggestion_id)

    return redirect('suggestion_list')