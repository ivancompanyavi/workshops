from django.contrib.auth.models import User
from django.db import models
import os
from workshops.settings import STATIC_URL
from user_profile.models import Achievement


class LevelPoints(object):
    CORRECT_ANSWER = 100
    CREATE_QUESTION = 200
    CREATE_WORKSHOP = 500


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
    achievements = models.ManyToManyField(Achievement, blank=True)
    experience = models.IntegerField(default=0)

    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        return os.path.join('profile_avatars', str(self.user.id) + '.' + extension)

    avatar = models.ImageField(upload_to=get_file_path)

    @property
    def level(self):
        finished = False
        starting_experience = 1000
        level_increase = 100
        current_level = 1
        exp = self.experience
        while not finished:
            if exp >= starting_experience * current_level + (current_level - 1) * level_increase:
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

    def __unicode__(self):
        return self.user.username