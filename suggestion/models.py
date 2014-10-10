from django.db import models
from core.models import Worker


class Suggestion(models.Model):
    NOT_STARTED = 'NS'
    IN_PROGRESS = 'IP'
    FINISHED = 'FN'
    STATUS_CHOICES = (
        (NOT_STARTED, 'Not started'),
        (IN_PROGRESS, 'in progress'),
        (FINISHED, 'Finished'),
    )
    suggester = models.ForeignKey(Worker, related_name='suggestions')
    message = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NOT_STARTED)

    def get_comments(self):
        return Comment.objects.filter(suggestion=self)


class Comment(models.Model):

    poster = models.ForeignKey(Worker, related_name='comments')
    message = models.TextField()
    suggestion = models.ForeignKey(Suggestion)