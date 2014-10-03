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
    suggester = models.ForeignKey(Worker)
    message = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NOT_STARTED)
