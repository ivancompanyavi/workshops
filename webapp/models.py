from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Option(models.Model):
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return self.description


class Question(models.Model):
    description = models.TextField()
    options = models.ManyToManyField(Option)

    def __unicode__(self):
        return self.description


class Workshop(models.Model):
    NOT_STARTED = 0
    FINISHED = 1
    CLOSED = 2
    STATUS_CHOICES = (
        (NOT_STARTED, 'not started'),
        (FINISHED, 'finished'),
        (CLOSED, 'closed')
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    prerequisites = models.TextField(blank=True)
    objectives = models.TextField()
    questions = models.ManyToManyField(Question)
    commiter = models.ForeignKey('Worker')

    def __unicode__(self):
        return self.name


class Achievement(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    points = models.IntegerField()
    image = models.ImageField(upload_to='achievement_images')

    def __unicode__(self):
        return self.name


class Worker(models.Model):
    MOLE = 1
    BEE = 2
    REAPER = 3
    TEAM_CHOICES = (
        (MOLE, 'Mole'),
        (BEE, 'Bee'),
        (REAPER, 'Reaper')
    )
    user = models.OneToOneField(User)
    team = models.IntegerField(choices=TEAM_CHOICES)
    workshops_subscribed = models.ManyToManyField(Workshop, related_name='subscriber', blank=True)
    achievements = models.ManyToManyField(Achievement, blank=True)
    experience = models.IntegerField(default=0)
    avatar = models.ImageField()

    @property
    def level(self):
        finished = False
        starting_experience = 100
        current_level = 1
        exp = self.experience
        while not finished:
            if exp >= starting_experience * current_level:
                current_level += 1
            else:
                finished = True

        return current_level

    def __unicode__(self):
        return self.user.username
