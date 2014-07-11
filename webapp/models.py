import os
from django.db import models
from django.contrib.auth.models import User
from workshops.settings import STATIC_URL
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image


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
    questions = models.ManyToManyField(Question, blank=True)
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
    user = models.ForeignKey(User)
    team = models.IntegerField(choices=TEAM_CHOICES)
    workshops_subscribed = models.ManyToManyField(Workshop, related_name='subscriber', blank=True)
    achievements = models.ManyToManyField(Achievement, blank=True)
    experience = models.IntegerField(default=0)

    def get_file_path(instance, filename):
        extension = filename.split('.')[-1]
        return os.path.join('profile_avatars', str(instance.user.id) + '.' + extension)

    avatar = models.ImageField(upload_to=get_file_path)

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

    def avatar_url(self):
        if not self.avatar:
            return os.path.join(STATIC_URL, 'images', 'noimage.png')
        else:
            return self.avatar.url
    """
    def save(self, *args, **kwargs):

        if not self.id and not self.avatar:
            return

        super(Worker, self).save(*args, **kwargs)

        size = (400, 300)
        image = Image.open(self.avatar)
        image = image.thumbnail(size, Image.ANTIALIAS)
        image.save(self.avatar.path)
    """


    def get_own_workshops(self):
        result = []
        try:
            result = Workshop.objects.filter(commiter_id=self.id)
        except ObjectDoesNotExist:
            pass
        return result

    def __unicode__(self):
        return self.user.username
