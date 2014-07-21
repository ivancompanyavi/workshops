from django.db import models
from core.models import Worker


class Suggestion(models.Model):
    suggester = models.ForeignKey(Worker)
    message = models.TextField()
